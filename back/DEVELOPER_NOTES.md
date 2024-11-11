## Estructura para sockets

Update (quedo medio viejo esto ya)

https://docs.google.com/document/d/1D1HnV5DHAZU_B9PtHppDibC6aPR1EXCGbVc7qoQAwFw/edit

## Estructura de los directorios

app.py (Endpoints del API)

models.py (estructura de la tabla de base de datos)

{directorio}_repository.py (Accesos y modificaciones a la base de datos)

schemas.py (Tipos de datos de las entradas y respuestas que nos lleguen de y mandemos al front)

socket_{directorio}.py (Donde hacemos todos los eventos que se hagan con socket.io)

utils.py (metodos de logica y algoritmos)

## Branches

### Crear una branch por cada epica (Puede haber una que no sea de una epica)

```
git checkout development

git checkout -b nombre_epica

git push origin nombre_epica
```

### Eliminar una branch

```
git checkout development

git branch -d nombre_del_branch

git push origin --delete nombre_del_branch
```

### Commitear a una branch

Asegurarse de estar parado en la branch correcta
```
git branch
```
Cuando vayan a hacer el pull usar origin

```
git push origin nombre_del_branch
```

### Merge con development
```
git checkout development

git merge nombre_epica

git push origin nombre_rama
```
### Pull

Indicar a q branch se quiere pullear
```
git pull origin nombre_rama
```
## Documentacion

En el siguiente exel

(https://docs.google.com/spreadsheets/d/1twD29F0e4ql25RZdRB2EyWdRLmIV7OXXSfJdfAAi_84/edit?usp=sharing)

## Endpoints

Poner los endpoints de la siguente manera

### RUTA

/directorio/endpoint

### METODO

Especificar el metodo POST, GET, PATCH, PUT, DELETE

### ENTRADA

Deben ser los mismos nombres definidos en schemas y models

### SALIDA

El schema que se envia de respuesta en response_model, por ejemplo

response_model=PartidaData

class PartidaData(BaseModel):
    id: int
    nombre: str
    owner: str
    iniciada: bool
    cantidad_jugadores: int
    color_bloqueado: str
    turno: int
    jugador1: str
    jugador2: str
    jugador3: str
    jugador4: str
    max_jugadores: int

### DESCRIPCION 

Duh

## Socket emits

### EVENTO

El mensaje que se emite por la room

## DONDE SE EMITE

Lugar donde se espera que se emita el mensaje, puede ser en / o en la room de la partida

## DESCRIPCION

duh

## EFECTO ESPERADO

Breve texto para que el fron sepa que se espera con ese emit
