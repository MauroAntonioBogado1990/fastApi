from email import message
from faulthandler import cancel_dump_traceback_later
from unicodedata import name
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel#creamos la base de model 
from typing import Optional #importamos para generar el valor de id
from uuid import uuid4 as uuid#importamos para tener el id unico
#creamos la aplicacion para comenzar

app = FastAPI()

#publicaciones donde se va a guardar los elementos
elemnts = []

#creamos la clase
class Element(BaseModel):
    id : Optional[str]
    name : str
    cant : int
    color : str

#creacion de la ruta de indices
@app.get('/')
def read_root():
    return {'Bienvenido a la API':   'Welcome to the API'}

#creamos la ruta de las publicaciones
@app.get('/posts')
def show_posts():
    return elemnts


#creamos ruta de la creacion de publicaciones
@app.post('/posts')
def create_posts(post: Element):
    post.id = str(uuid())#creamos el id unico
    elemnts.append(post.dict())#agregamos el elemento al arreglo
    print(post.dict())#crea la manera de que se vea como diccionario de clave-valor
    return elemnts[-1]

#creamos get de retorno de id
@app.get('/posts/{post_id}')
def get_post_id(post_id :str):
    for e in elemnts:
        if e["id"] == post_id:
            return e
    raise HTTPException(status_code=404, detail='Post not found')

@app.delete('/posts/{post_id}')
def delete_post(post_id :str):
    for i,e in elemnts:
        if e["id"] == post_id:
            elemnts.pop(i)
            return {'message':'Post deleted successfully'}
    raise HTTPException(status_code=404, detail='Post deleted')

#creamos ruta para actualizar
@app.put('/posts/{post_id}')
def update_post(post_id :str, updateElement: Element):
    for index, ele in enumerate(elemnts):
        if ele["id"]   == post_id:
            Element[id]["name"] == updateElement.name
            Element[id]["cant"] == updateElement.cant
            Element[id]["color"] == updateElement.color
            return {'message':'Post updated successfully'}    
    raise HTTPException(status_code=404, detail='Post deleted')
 


    

