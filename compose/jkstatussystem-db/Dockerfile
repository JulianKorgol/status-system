FROM mariadb:latest

ENV MARIADB_ROOT_PASSWORD=test123

RUN mkdir -p /docker-entrypoint-initdb.d

COPY /sql/db.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
