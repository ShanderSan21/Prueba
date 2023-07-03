# Importamos los paquetes que vamos a utilizar
from fastapi import FastAPI
import uvicorn

# Importamos las funciones creadas en openaitest
from openaitest import Document

# Asignamos el nombre a la variable de la API
app = FastAPI()

# Generamos el primer mensaje en la raíz 127.0.0.1/
@app.get("/")
def read_root():
    return {"Hola": "Bienvenido"}

    # Generamos la función endpoint en FastAPI
@app.post('/inference', status_code=200)
def inference_endpoint(doc: Document):
    response = Document.inference(doc.prompt)
    return {
                'inference': response[0],
                 'usage': response[1]
                            }

#EJECUTAMOS EL API SIN LA TERMINAL CON UN NUMERO DE PUERTO
if __name__ == '__main__':
    uvicorn.run("main:app",port=9042)
