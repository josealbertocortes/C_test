# Test Microserivcios
## Preinstalaciones
Es necesario tener git y docker instalado para esta prueba 
###### Clonar el repositorio 
`git clone https://github.com/josealbertocortes/C_test.git`

## Microservicio uno 
Es necesario estar en la raiz del repositorio 
##### Ir a la carpeta de fastApiMarvel
`cd fastApiMarvel`
##### Variables de entorno
En la carpeta fastApiMarvel se encuentro un archivo .env.example como ejemplo con las variables a agregar.
###### Crear el archivo .env 
`touch .env`

Agregar la siguiente informaión  en el archivo .env 

    BASE_URL='https://gateway.marvel.com/v1/public/'
    PUBLIC = 'public_key_marvel'
    PRIVATE = 'private_key_marvel'
    TS='1'

##### Ejecutar el siguiente comando
`docker build -t microserviciouno  .`

`docker run -d --name microserviciodoss -p 8000:8000 microserviciouno`

##### Documentacion de la apis 
En la siguiente url se encuentra la documentación generada por fastapi 

http://127.0.0.1:8000/docs

## Microservicio dos 
Es necesario estar en la raiz del repositorio 
##### Ir a la carpeta de fastApiMongo
`cd fastApiMongo`

##### Variables de entorno
En la carpeta fastApiMongo se encuentro un archivo .env.example como ejemplo con las variables a agregar.
###### Crear el archivo .env 
`touch .env`

Agregar la siguiente informaión  en el archivo .env 

    URLCONEXIONMONGO="mongodb+srv://<usuario>:<contrasenn>@fastapi.tvmaijk.mongodb.net/?retryWrites=true&w=majority"

##### Ejecutar el siguiente comando

`docker build -t microserviciodos  .`

`docker run -d --name microserviciodos -p 7000:7000 microserviciodos`

##### Documentacion de la apis 
En la siguiente url se encuentra la documentación generada por fastapi 

http://127.0.0.1:7000/docs
