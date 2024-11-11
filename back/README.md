Proyecto de ingenieria del software I de la facultad de F.A.M.A.F de la Universidad Nacional de Cordoba

Nombre de grupo = AvengersAssembly

Instrucciones para levantar el servidor de backend y la base de datos

### Requisitos Previos
Asegúrate de tener los siguientes requisitos previos instalados antes de continuar:

- Python 3.10.12
- Entorno virtual (recomendamos venv)
- pip
- uvicorn
- mysql

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

# Testeos

Ejecutar testeos con 

```
pytest
```