from fastapi import FastAPI

#creamos la aplicacion para comenzar

app = FastAPI()

#publicaciones donde se va a guardar los elementos
posts = []

#creacion de la ruta de indices
@app.get('/')
def read_root():
    return {'Bienvenido a la API':   'Welcome to the API'}

#creamos la ruta de las publicaciones
@app.get('/posts')
def show_posts():
    return posts


#creamos ruta de la creacion de publicaciones
@app.post('/posts')
def create_posts(post):
    print(posts)
    return "recieved"


