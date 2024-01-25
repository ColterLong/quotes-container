FROM mysql:8.3.0

COPY schema.sql /docker-entrypoint-initdb.d/schema.sql

ARG MYSQL_DATABASE

RUN sed -i "s/MYSQL_DATABASE/$MYSQL_DATABASE/g" /docker-entrypoint-initdb.d/schema.sql

EXPOSE 3306