
# This is for an actual cloud server
# FROM mariadb:latest

# This is specifically for a raspberry pi
FROM jsurf/rpi-mariadb:latest

RUN apt-get update && \
    apt-get install --no-install-recommends -y 


RUN touch /var/log/mysql/mysqld.log