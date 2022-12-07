import pika 
import time 
import json
import requests

# log_file = open("/var/log/my_project/receiver/receiver.log","a")
# config_file = open("/etc/my_project/receiver/receiver.yaml","r")
# config = yaml.load(config_file)

# pika_username = config["rabbitmq"]["username"]
# pika_password = base64.b64decode(config["rabbitmq"]["password"])
# pika_addr = config["rabbitmq"]["host"]
# pika_port = config["rabbitmq"]["port"]
# pika_virtualhost = config["rabbitmq"]["virtualhost"]
# pika_queue = config["rabbitmq"]["queue"]
pika_username = "guest"
pika_password = "guest"
pika_addr = "rabbitmq"
pika_port = "5672"
pika_virtualhost = "virtualhost"
pika_queue = "queue"

print(' [*] Waiting for rabbitMQ 30s')
time.sleep(30)
print(' [*] Ready')

credentials = pika.PlainCredentials(pika_username, pika_password)
parameters  = pika.ConnectionParameters(pika_addr, pika_port, pika_virtualhost, credentials)
connection  = pika.BlockingConnection(parameters)
channel     = connection.channel()

channel.queue_declare(queue=pika_queue, durable=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):


    print(" [x] Received %r" % (json.loads(body))) #this goes to stdout

    url = 'http://127.0.0.1:8000/appeal'
    myobj = json.loads(body) #{'somekey': 'somevalue'}
    x = requests.post(url, json = myobj)
    # print(x.text)
    
    time.sleep(1)
    channel.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(pika_queue, callback)
channel.start_consuming()