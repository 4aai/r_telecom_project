FROM debian

RUN apt update
RUN apt install -y python python3-pip
RUN apt clean

EXPOSE 8888

WORKDIR /app

RUN pip3 install pika tornado

COPY . .

CMD [ "python3", "app.py"]