# fastapi-crud-mysql
A simple CRUD operation with FastAPI, Python and MySQL DB, providing a powerful RESTFul API.

More at: https://medium.com/@emergeit/database-crud-with-fastapi-keep-it-simple-and-documented-with-python-and-mysql-db-7d626520c37a


## How to start:

Must have: Docker and Docker-compose.


1. cd fastapi-crud-mysql/infrastructure
2. docker-compose up -d

Wait until all libs are installed.

Then you can access:
1. PhpMyAdmin: Port 8088;
2. FastAPI: Port 8000;
3. MySQL: Port 3306;


The API docs you can access with:
localhost:8000/docs

### Credentials:

1. [PhpMyAdmin] 	 root - 123123
2. [MySQL]			 root - 123123
3. [FastAPI/Swagger] brunow - superTest
