FROM debian

RUN apt update
RUN apt install -y python3 python3-pip
RUN apt install -y libmariadb3 libmariadb-dev
RUN apt clean

EXPOSE 8888

WORKDIR /app

RUN pip3 install pika 
RUN pip3 install fastapi 
RUN pip3 install mariadb
RUN pip3 install requests
RUN pip3 install databases
RUN pip3 install aiomysql
RUN pip3 install uvicorn

COPY . .

CMD ["uvicorn", "main:app"]