from fastapi import FastAPI

app = FastAPI()


@app.get('/',tags=["Usuarios"])
def home():
    return "USUARIOS REGISTRADOS"

@app.get('/listar',tags=["Usuarios"])
def homelistar():
    return "LISTAS USUARIOS"
