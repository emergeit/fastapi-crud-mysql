# fastapi-crud-mysql
A simple CRUD operation with FastAPI, Python and MySQL DB, providing a powerful RESTFul API.

More at: https://medium.com/@emergeit/database-crud-with-fastapi-keep-it-simple-and-documented-with-python-and-mysql-db-7d626520c37a


## How to start:

#### Must have: Docker and Docker-compose.


1. cd fastapi-crud-mysql/infrastructure
2. docker-compose up -d

#### Wait until all libs are installed.

Then you can access:
1. PhpMyAdmin: Port 8088;
2. FastAPI: Port 8000;
3. MySQL: Port 3306;


The API docs you can access with:
localhost:8000/docs

#### Credentials:

1. [PhpMyAdmin] 	 root - 123123
2. [MySQL]			 root - 123123
3. [FastAPI/Swagger] brunow - superTest

#### How to know if we're done
docker logs fastapi-poc-python3-app

This output should be like this:

![image](https://user-images.githubusercontent.com/87096896/156464775-ba28ad45-8f3c-463a-aa31-cfdc68146fc9.png)


Remember: Port 8000 isnt be able to access until the container stop to process the initial installations.
After it we could use.
