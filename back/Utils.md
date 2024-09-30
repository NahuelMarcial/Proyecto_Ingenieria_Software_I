## Estructura para sockets

https://docs.google.com/document/d/1D1HnV5DHAZU_B9PtHppDibC6aPR1EXCGbVc7qoQAwFw/edit

## Estructura de los directorios

models.py (estructura de la tabla de base de datos y métodos lógicos tipo hacer el shuffle y todo eso)

view.py (Endpoints del API y los metodos que sirvan para eso q solo sean querys y cosas asi)

schemas.py (Tipos de datos de las entradas y respuestas que nos lleguen de y mandemos al front)

socket_{nombre del directorio}.py (Donde hacemos todos los eventos que se hagan con websocket)

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

(cuando el tomi mande el link editable jeje)

Poner los endpoints de la siguente manera

### RUTA

/directorio/endpoint

### METODO

Especificar el metodo POST, GET, PATCH, PUT, DELETE

En lo posible no hacer un endpoint que haga mas de una de las anteriores

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