import hashlib
from enum import Enum
from fastapi import FastAPI, Response, status
import requests
from app.server.getData import change_payload_characters,change_payload_comics,get_resquest_comic,get_resquest_personajes
import os
from dotenv import load_dotenv

load_dotenv()

public = os.getenv('PUBLIC')
private = os.getenv('PRIVATE')
ts = os.getenv('TS')
h = hashlib.md5((ts + private + public).encode()).hexdigest()
base = os.getenv('BASE_URL')


class ToSearch(str, Enum):
    personajes = "personajes"
    comic = "comic"


app = FastAPI()


@app.get("/searchComics")
def get_general(response: Response, skip: int = 0, limit: int = 10):

    personajes = requests.get(base + 'characters',
                              params={'apikey': public,
                                      'ts': ts,
                                      "offset": skip,
                                      "limit": limit,
                                      'hash': h}).json()
    if personajes["code"] == 200:
        data = change_payload_characters(personajes)
        response.status_code = status.HTTP_200_OK
        return {"personajes": data}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"details": "Error al realizar la peticion"}


@app.get("/searchComics/{searchParam}", status_code=200)
def get_model(response: Response, searchParam: ToSearch, name: str = "", skip: int = 0, limit: int = 10):
    if searchParam.value == "personajes":
        return get_resquest_personajes(name, response, skip, limit)

    if searchParam.value == "comic":
        return get_resquest_comic(name, response, skip, limit)
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"details": "No se encuentra la ruta registrada"}
