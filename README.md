# fastapi-crud-mysql
A simple CRUD operation with FastAPI, Python and MySQL DB, providing a powerful RESTFul API.

More at: https://medium.com/@emergeit/database-crud-with-fastapi-keep-it-simple-and-documented-with-python-and-mysql-db-7d626520c37a


## How to start:

Must have: Docker and Docker-compose.


1. cd fastapi-crud-mysql/infrastructure
2. docker-compose up -d

Wait until all libs are installed.

Then you can access:
PhpMyAdmin: Port 8088;
FastAPI: Port 8000;
MySQL: Port 3306;


The API docs you can access with:
localhost:8000/docs

### Credentials:
PhpMyAdmin  	| root - 123123
MySQL 			| root - 123123
FastAPI/Swagger | brunow - superTest
