import requests
import hashlib
from fastapi import status
import os
from dotenv import load_dotenv

load_dotenv()

public = os.getenv('PUBLIC')
private = os.getenv('PRIVATE')
ts = os.getenv('TS')
h = hashlib.md5((ts + private + public).encode()).hexdigest()
base = os.getenv('BASE_URL')


def change_payload_characters(personajes):
    data = personajes["data"]["results"]
    data = [{"id": personaje["id"], "name":personaje["name"], "aparances":personaje["comics"]
             ["available"], "image":personaje["resourceURI"]} for personaje in data]
    return data


def get_resquest_personajes(name, response, skip, limit):
    if name == "":
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
    else:
        personajes = requests.get(base + 'characters',
                                  params={'apikey': public,
                                          'ts': ts,
                                          "nameStartsWith": name,
                                          'hash': h}).json()
        if personajes["code"] == 200:
            data = change_payload_characters(personajes)
            response.status_code = status.HTTP_200_OK
            return {"personajes": data}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"details": "Error al realizar la peticion"}


def change_payload_comics(comics):
    data = comics["data"]["results"]
    print(data)

    data = [{"id": comic["id"], "title":comic["title"], "date":comic["dates"]
             [0]["date"], "image":comic["resourceURI"]} for comic in data]
    return data


def get_resquest_comic(name, response, skip, limit):
    if name == "":
        comics = requests.get(base + 'comics',
                              params={'apikey': public,
                                      'ts': ts,
                                      "format": "comic",
                                      "offset": skip,
                                      "limit": limit,
                                      'hash': h}).json()
        if comics["code"] == 200:
            data = change_payload_comics(comics)
            response.status_code = status.HTTP_200_OK
            return {"comics": data}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"details": "Error al realizar la peticion"}
    else:
        comics = requests.get(base + 'comics',
                              params={'apikey': public,
                                      'ts': ts,
                                      "format": "comic",
                                      "titleStartsWith": name,
                                      'hash': h}).json()

        if comics["code"] == 200:
            data = change_payload_comics(comics)
            response.status_code = status.HTTP_200_OK
            return {"comics": data}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"details": "Error al realizar la peticion"}
