from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

person = APIRouter()
persons = [

]
class models_person(BaseModel):
    id:str
    nombre:str
    primer_apellido: str
    segundo_apellido: str
    direccion: str
    telefono:str
    correo: str
    sangre: str
    fecha_nacimiento: datetime
    created_at:datetime = datetime.now()
    estatus:bool=False

@person.get("/")

def bienvenido():
    return "Hola 9B"

@person.get("/person", tags=['Personas'])

def getPerson():
    return persons

@person.post("/person/{person_id}", tags=['Personas'])

def postPerson(person_id: str):
    for person in persons:
        if person.id == person_id:
            return person

@person.post('/person', tags=['Personas'])

def insertPerson(insert_person:models_person):
    persons.append(insert_person)
    return {"message": f"Se ha insertado un nuevo usuario con el ID: {insert_person.id}"}

@person.put('/person/{person_id}', tags=['Personas'])

def updatePerson(update_person:models_person, person_id: str):
    print(update_person)
    for index, person in enumerate(persons):
        if person.id == person_id:
            update_person.created_at = person.created_at
        
            persons[index] = update_person
            
            return {"message": f"Se ha modificado correctamente a la persona con el ID: {person_id}"}

@person.delete('/person/{person_id}', tags=['Personas'])

def deletePerson(person_id: str):
    for index, person in enumerate(persons):
        if person.id == person_id:
            persons.pop(index)
            return {"message": f"Se ha eliminado correctamente a la persona con el ID: {person_id}"}

