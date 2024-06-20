#Importaciones
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

user = APIRouter()
users = []

#userModel
class model_user(BaseModel): #Creacion de un modelo de datos
    id:str
    usuario:str
    password:str
    created_at:datetime = datetime.now  #Formato de fecha y hora
    estatus:bool=False
    
@user.get("/")

def bienvenido():
    return "Bienvenido al sistema de APIS"


@user.get("/users")

def get_usuarios():
    return users        #Retornar todos los usuarios

@user.post("/users")

def save_usuarios(users:model_user):
    #users.append
    print (users)
    return "Datos guardados"