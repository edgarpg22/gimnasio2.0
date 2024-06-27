from fastapi import APIRouter, Depends
import schemas, models
from cruds import crud
from sqlalchemy.orm import Session
from config.db import SessionLocal, engine


user = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user.get("/", tags=['Usuarios'])

def bienvenido():
    return "Bienvenido al sistema de apis"

@user.get("/users", response_model=list[schemas.users], tags=['Usuarios'])

def get_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip = skip, limit = limit)
    return users
@user.post("/users/{user_id}", tags=['Usuarios'])

def postUser(user_id: str):
    for user in users:
        if user.id == user_id:
            return user

@user.post('/users', tags=['Usuarios'])

def insertUser(insert_user:models_user):
    users.append(insert_user)
    return {"message": f"Se ha insertado un nuevo usuario con el ID: {insert_user.id}"}

@user.put('/users/{user_id}', tags=['Usuarios'])

def updateUser(update_user:models_user, user_id: str):
    print(update_user)
    for index, user in enumerate(users):
        if user.id == user_id:
            update_user.created_at = user.created_at
        
            users[index] = update_user
            
            return {"message": f"Se ha modificado correctamente al usuario con el ID: {user_id}"}

@user.delete('/users/{user_id}', tags=['Usuarios'])

def deleteUser(user_id: str):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {"message": f"Se ha eliminado correctamente al usuario con el ID: {user_id}"}





# #Importaciones
# from fastapi import APIRouter
# from pydantic import BaseModel
# from datetime import datetime

# user = APIRouter()
# users = []

# #userModel
# class model_user(BaseModel): #Creacion de un modelo de datos
#     id:str
#     usuario:str
#     password:str
#     created_at:datetime = datetime.now  #Formato de fecha y hora
#     estatus:bool=False
    
# @user.get("/")

# def bienvenido():
#     return "Bienvenido al sistema de APIS"


# @user.get("/users")

# def get_usuarios():
#     return users        #Retornar todos los usuarios

# @user.post("/users")

# def save_usuarios(insert_users:model_user):
#     users.append(insert_users)
#     #print (insert_users)
#     return "Datos guardados"