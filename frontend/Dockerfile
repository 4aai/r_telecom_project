FROM debian
RUN apt update
RUN apt install -y apache2
RUN apt install -y apache2-utils
RUN apt clean
EXPOSE 80
WORKDIR /var/www/html
COPY . .
CMD [ "apache2ctl", "-D", "FOREGROUND" ]
