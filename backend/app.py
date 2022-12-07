# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
import pika

# config_file = open("/etc/my_project/sender/sender.yaml","r")
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


def send_message_rabbitmq(message="Hello World!"):
    credentials = pika.PlainCredentials(pika_username, pika_password)
    parameters = pika.ConnectionParameters(pika_addr, pika_port, pika_virtualhost, credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=pika_queue, durable=True)
    channel.basic_publish(exchange='',
                          routing_key=pika_queue,
                          body=message,
                          properties=pika.BasicProperties(
                             delivery_mode=2,
                          ))
    connection.close()


class MyHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        # print('set headers!!')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        data = tornado.escape.json_decode(self.request.body) 
        print('================================')
        print('Got JSON data:', data)
        print('Last Name :', data['lname'])
        print('First Name :', data['fname'])
        print('Patronymic Name :', data['pname'])
        print('Phone number :', data['phone'])
        print('Message :', data['message'])

        send_message_rabbitmq(tornado.escape.json_encode(data))

        self.write({ 'got' : 'your data' })

if __name__ == '__main__':
    app = tornado.web.Application([ tornado.web.url(r'/', MyHandler) ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    print('Starting server on port 8888')
    tornado.ioloop.IOLoop.instance().start()