Instrucciones para levantar el servidor de backend y la base de datos

### Requisitos Previos
Asegúrate de tener los siguientes requisitos previos instalados antes de continuar:

- Python 3.10.12
- Entorno virtual (recomendamos venv)
- pip
- uvicorn
- mysql

# Servidor de base de datos

1) Descargar/actualizar la imagen de mysql en docker si no lo tiene

En una terminal
```
sudo docker pull mysql
```
2) Creamos un docker de la siguiente manera (check  :3306)

```
sudo docker run --name db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql
```

3) Entramos al docker

```
sudo docker exec -it db bash
```

4) Dentro del docker ingresar a mysql con

```
mysql -p
```

5) Ingresar contraseña 123456

6) Crear base de datos

```
create database db;
```

7) Usar la base de datos (checkear si hace falta)

```
use db;
```

8) Al cerrar, cerrar el docker

```
sudo docker stop db
```

9) Eliminar el docker

```
sudo docker rm db
```

# Servidor Backend

1) Clona este repositorio.

2) Ingresa a la carpeta del proyecto

3) Crea un entorno virtual con Python 3.10.12.

```
python3 -m venv venv
```

4) Activa el entorno virtual.

```
source venv/bin/activate
```
5) Instala las dependencias con:

```
pip install -r requirements.txt
```

6) Inicia el servidor con

```
uvicorn app.main:app --reload
```

7) Revisar aplicación front en localhost:8000 en el navegador web

