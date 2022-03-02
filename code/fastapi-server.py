import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Optional
import logging as logger
import random
import uuid
from db import Database
from datetime import datetime

app = FastAPI(
    title="Calls API",
    description="""Utilizado para capturar ligações do fornecedor X em Y banco.<br/>
                   Para maiores informações e acessos por favor entre em contato com
                   o setor de tecnologia.""",
)
security = HTTPBasic()
db = Database()


def validateLogin(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "brunow")
    correct_password = secrets.compare_digest(credentials.password, "superTest")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Os dados estão incorretos. Favor revisar a assinatura e/ou credenciais.",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/", tags=["Rota Padrão"])
async def read_initial_api_test(username: str = Depends(validateLogin)):
    return {
        "Welcome to FastAPI Poc - Bruno Cardoso Farias -> 01/03/2022 ": "Status [OK]"
    }


## ______________________________ ## ______________________________ ##
# CREATE
@app.post("/call/", tags=["Calls"])
async def create_call(
    midia_id: int = random.choice([1, 2]),
    user_id: int = random.choice([1, 2]),
    customer_id: int = random.choice([1, 2, 3]),
    tipo_id: int = random.choice([1, 2, 3]),
    project_id: int = random.choice([1, 2, 3, 4]),
    status_id: int = random.choice([1, 2, 3, 4]),
    nm_protocol: str = str(uuid.uuid4()),
    qtd_minutos_call: int = random.randint(1, 60),
    created_at: str = "NOW()",
    updated_at: str = "null",
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""INSERT INTO tb_call 
        (midia_id, user_id, customer_id, tipo_id, project_id, status_id, nm_protocol, qtd_minutos_call, created_at, updated_at)
        VALUES ({midia_id}, {user_id}, {customer_id}, {tipo_id}, {project_id}, {status_id}, "{nm_protocol}", {qtd_minutos_call}, {created_at}, {updated_at})
        """,
        autoCommit=True,
    )


# READ
@app.get("/call", tags=["Calls"])
async def read_call(
    id: Optional[int] = None,
    count: Optional[bool] = None,
    username: str = Depends(validateLogin),
):
    if count == True:
        return db.query(query="SELECT count(*) as count FROM tb_call;")
    if id is None:
        return db.query(query="SELECT * FROM tb_call LIMIT 100;")
    else:
        return db.query(query=f"SELECT * FROM tb_call WHERE id = {id};")


# UPDATE
@app.put("/call/{id}", tags=["Calls"])
async def update_call(
    id: int,
    midia_id: int = random.choice([1, 2]),
    user_id: int = random.choice([1, 2]),
    customer_id: int = random.choice([1, 2, 3]),
    tipo_id: int = random.choice([1, 2, 3]),
    project_id: int = random.choice([1, 2, 3, 4]),
    status_id: int = random.choice([1, 2, 3, 4]),
    nm_protocol: str = str(uuid.uuid4()),
    qtd_minutos_call: int = random.randint(1, 60),
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""UPDATE tb_call SET
            midia_id = {midia_id},
            user_id = {user_id},
            customer_id = {customer_id},
            tipo_id = {tipo_id},
            project_id = {project_id},
            status_id = {status_id},
            nm_protocol = "{nm_protocol}",
            qtd_minutos_call = {qtd_minutos_call}
            WHERE id = {id};
        """,
        autoCommit=True,
    )


# DELETE
@app.delete("/call/{id}", tags=["Calls"])
async def delete_call(id: int, username: str = Depends(validateLogin)):
    return db.query(query=f"DELETE FROM tb_call WHERE id = {id};", autoCommit=True)


## ______________________________ ## ______________________________ ##
# CREATE
@app.post("/call_status/", tags=["Calls Status"])
async def create_call_status(
    nm_status: str,
    st_status: int = random.choice([0, 1]),
    created_at: str = "NOW()",
    updated_at: str = "null",
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""INSERT INTO tb_call_status 
        (nm_status, st_status, created_at, updated_at)
        VALUES ("{nm_status}", {st_status}, {created_at}, {updated_at})
        """,
        autoCommit=True,
    )


# READ
@app.get("/call_status", tags=["Calls Status"])
async def read_call_status(
    id: Optional[int] = None,
    count: Optional[bool] = None,
    username: str = Depends(validateLogin),
):
    if count == True:
        return db.query(query="SELECT count(*) as count FROM tb_call_status;")
    if id is None:
        return db.query(query="SELECT * FROM tb_call_status;")
    else:
        return db.query(query=f"SELECT * FROM tb_call_status WHERE id = {id};")


# UPDATE
@app.put("/call_status/{id}", tags=["Calls Status"])
async def update_call_status(
    id: int,
    nm_status: str,
    st_status: int = random.choice([0, 1]),
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""UPDATE tb_call_status SET
            nm_status = "{nm_status}",
            st_status = {st_status},
            WHERE id = {id};
        """,
        autoCommit=True,
    )


# DELETE
@app.delete("/call_status/{id}", tags=["Calls Status"])
async def delete_call_status(id: int, username: str = Depends(validateLogin)):
    return db.query(
        query=f"DELETE FROM tb_call_status WHERE id = {id};", autoCommit=True
    )


## ______________________________ ## ______________________________ ##
# CREATE
@app.post("/call_tipo/", tags=["Calls Tipo"])
async def create_call_tipo(
    nm_tipo: str,
    st_tipo: int = random.choice([0, 1]),
    created_at: str = "NOW()",
    updated_at: str = "null",
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""INSERT INTO tb_call_tipo 
        (nm_tipo, st_tipo, created_at, updated_at)
        VALUES ("{nm_tipo}", {st_tipo}, {created_at}, {updated_at})
        """,
        autoCommit=True,
    )


# READ
@app.get("/call_tipo", tags=["Calls Tipo"])
async def read_call_tipo(
    id: Optional[int] = None,
    count: Optional[bool] = None,
    username: str = Depends(validateLogin),
):
    if count == True:
        return db.query(query="SELECT count(*) as count FROM tb_call_tipo;")
    if id is None:
        return db.query(query="SELECT * FROM tb_call_tipo;")
    else:
        return db.query(query=f"SELECT * FROM tb_call_tipo WHERE id = {id};")


# UPDATE
@app.put("/call_tipo/{id}", tags=["Calls Tipo"])
async def update_call_tipo(
    id: int,
    nm_tipo: str,
    st_tipo: int = random.choice([0, 1]),
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""UPDATE tb_call_tipo SET
            nm_tipo = "{nm_tipo}",
            st_tipo = {st_tipo},
            WHERE id = {id};
        """,
        autoCommit=True,
    )


# DELETE
@app.delete("/call_tipo/{id}", tags=["Calls Tipo"])
async def delete_call_tipo(id: int, username: str = Depends(validateLogin)):
    return db.query(query=f"DELETE FROM tb_call_tipo WHERE id = {id};", autoCommit=True)


## ______________________________ ## ______________________________ ##
# CREATE
@app.post("/customer/", tags=["Customers"])
async def create_customer(
    nm_customer: str,
    nm_sexo: int = random.choice(["M", "F", "I"]),
    created_at: str = "NOW()",
    updated_at: str = "null",
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""INSERT INTO tb_customer 
        (nm_customer, nm_sexo, created_at, updated_at)
        VALUES ("{nm_customer}", "{nm_sexo}", {created_at}, {updated_at})
        """,
        autoCommit=True,
    )


# READ
@app.get("/customer", tags=["Customers"])
async def read_customer(
    id: Optional[int] = None,
    count: Optional[bool] = None,
    username: str = Depends(validateLogin),
):
    if count == True:
        return db.query(query="SELECT count(*) as count FROM tb_customer;")
    if id is None:
        return db.query(query="SELECT * FROM tb_customer;")
    else:
        return db.query(query=f"SELECT * FROM tb_customer WHERE id = {id};")


# UPDATE
@app.put("/customer/{id}", tags=["Customers"])
async def update_customer(
    id: int,
    nm_tipo: str,
    st_tipo: int = random.choice([0, 1]),
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""UPDATE tb_customer SET
            nm_tipo = "{nm_tipo}",
            st_tipo = {st_tipo},
            WHERE id = {id};
        """,
        autoCommit=True,
    )


# DELETE
@app.delete("/customer/{id}", tags=["Customers"])
async def delete_customer(id: int, username: str = Depends(validateLogin)):
    return db.query(query=f"DELETE FROM tb_customer WHERE id = {id};", autoCommit=True)


## ______________________________ ## ______________________________ ##
# CREATE
@app.post("/midia/", tags=["Midia"])
async def create_midia(
    nm_midia: str,
    nm_campanha: str,
    nm_fonte: str,
    nm_pagina: str,
    created_at: str = "NOW()",
    updated_at: str = "null",
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""INSERT INTO tb_midia 
        (nm_midia, nm_campanha, nm_fonte, nm_pagina, created_at, updated_at)
        VALUES ("{nm_midia}", "{nm_campanha}", "{nm_fonte}", "{nm_pagina}", {created_at}, {updated_at})
        """,
        autoCommit=True,
    )


# READ
@app.get("/midia", tags=["Midia"])
async def read_midia(
    id: Optional[int] = None,
    count: Optional[bool] = None,
    username: str = Depends(validateLogin),
):
    if count == True:
        return db.query(query="SELECT count(*) as count FROM tb_midia;")
    if id is None:
        return db.query(query="SELECT * FROM tb_midia;")
    else:
        return db.query(query=f"SELECT * FROM tb_midia WHERE id = {id};")


# UPDATE
@app.put("/midia/{id}", tags=["Midia"])
async def update_midia(
    id: int,
    nm_midia: str,
    nm_campanha: str,
    nm_fonte: str,
    nm_pagina: str,
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""UPDATE tb_midia SET
            nm_midia = "{nm_midia}",
            nm_campanha = "{nm_campanha}",
            nm_fonte = "{nm_fonte}",
            nm_pagina = {nm_pagina},
            WHERE id = {id}
        """,
        autoCommit=True,
    )


# DELETE
@app.delete("/midia/{id}", tags=["Midia"])
async def delete_midia(id: int, username: str = Depends(validateLogin)):
    return db.query(query=f"DELETE FROM tb_midia WHERE id = {id};", autoCommit=True)


## ______________________________ ## ______________________________ ##
# CREATE
@app.post("/project/", tags=["Projetos"])
async def create_project(
    nm_project: str,
    st_project: int = random.choice([0, 1]),
    created_at: str = "NOW()",
    updated_at: str = "null",
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""INSERT INTO tb_project 
        (nm_project, st_project, created_at, updated_at)
        VALUES ("{nm_project}", {st_project}, {created_at}, {updated_at})
        """,
        autoCommit=True,
    )


# READ
@app.get("/project", tags=["Projetos"])
async def read_project(
    id: Optional[int] = None,
    count: Optional[bool] = None,
    username: str = Depends(validateLogin),
):
    if count == True:
        return db.query(query="SELECT count(*) as count FROM tb_project;")
    if id is None:
        return db.query(query="SELECT * FROM tb_project;")
    else:
        return db.query(query=f"SELECT * FROM tb_project WHERE id = {id};")


# UPDATE
@app.put("/project/{id}", tags=["Projetos"])
async def update_project(
    id: int,
    nm_project: str,
    st_project: int = random.choice([0, 1]),
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""UPDATE tb_project SET
            nm_project = "{nm_project}",
            st_project = {st_project},
            WHERE id = {id}
        """,
        autoCommit=True,
    )


# DELETE
@app.delete("/project/{id}", tags=["Projetos"])
async def delete_project(id: int, username: str = Depends(validateLogin)):
    return db.query(query=f"DELETE FROM tb_project WHERE id = {id};", autoCommit=True)


## ______________________________ ## ______________________________ ##
# CREATE
@app.post("/user/", tags=["Users"])
async def create_user(
    nm_user: str,
    nm_completo: str,
    created_at: str = "NOW()",
    updated_at: str = "null",
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""INSERT INTO tb_user
        (nm_user, nm_completo, created_at, updated_at)
        VALUES ("{nm_user}", "{nm_completo}", {created_at}, {updated_at})
        """,
        autoCommit=True,
    )


# READ
@app.get("/user", tags=["Users"])
async def read_user(
    id: Optional[int] = None,
    count: Optional[bool] = None,
    username: str = Depends(validateLogin),
):
    if count == True:
        return db.query(query="SELECT count(*) as count FROM tb_user;")
    if id is None:
        return db.query(query="SELECT * FROM tb_user;")
    else:
        return db.query(query=f"SELECT * FROM tb_user WHERE id = {id};")


# UPDATE
@app.put("/user/{id}", tags=["Users"])
async def update_user(
    id: int,
    nm_user: str,
    nm_completo: str,
    username: str = Depends(validateLogin),
):
    return db.query(
        query=f"""UPDATE tb_user SET
            nm_user = "{nm_user}",
            nm_completo = {nm_completo},
            WHERE id = {id}
        """,
        autoCommit=True,
    )


# DELETE
@app.delete("/user/{id}", tags=["Users"])
async def delete_project(id: int, username: str = Depends(validateLogin)):
    return db.query(query=f"DELETE FROM tb_user WHERE id = {id};", autoCommit=True)


## ______________________________ ## ______________________________ ##
