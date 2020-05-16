FROM mysql:8.0.20

ENV MYSQL_DATABASE mydb

RUN apt-get update -y

COPY /script_sql/ /docker-entrypoint-initdb.d/