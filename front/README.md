# Proyecto - El Switcher online

## Descripción

Este es un proyecto de una página web para jugar un juego de mesa online, desarrollado utilizando **React** con **Vite** como base para el frontend, y **FastAPI** en el backend. El objetivo es ofrecer una plataforma donde los usuarios puedan conectarse y jugar en tiempo real.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Node.js** (v20 o superior)
- **npm** como manejador de paquetes
- **Git** para el control de versiones

## Instalación

Sigue estos pasos para clonar y configurar el proyecto en tu entorno local:

1. Clona este repositorio:

```bash
git clone https://github.com/IngSoft1-AvengersAssembly/front.git
```

2. Navega al directorio del proyecto:

```bash
cd frontend-switcher
```

3. Instala las dependencias necesarias:

``` bash
npm install
```

4. Inicia el servidor de desarrollo:

```bash
npm run dev
```

5. Abre tu navegador y visita la dirección: http://localhost:5173/

<<<<<<< HEAD
=======
```link
http://localhost:5173/
```
Deberias ver la pagina "Hola mundo!", ya que se trata de la branch 'dev' y en ella solo esta subido el repositorio base del proyecto.
>>>>>>> dev

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```php
├── node_modules/       # Dependencias del proyecto
├── public/             # Archivos públicos (index.html)
├── src/
│   ├── principal       # Archivos relacionados a la pagina principal
│   │   ├── components/     # Componentes presentacionales reutilizables
│   │   ├── containers/     # Containers que contienen la lógica de negocio
│   │   ├── services/       # Servicios externos como las llamadas a la API
│   ├── lobby           # Archivos relacionados a la sala de espera del juego
│   │   ├── components/   
│   │   ├── containers/     
│   │   ├── services/
│   ├── game           # Archivos relacionados a la partida
│   │   ├── components/     # Componentes presentacionales reutilizables
│   │   ├── containers/     # Containers que contienen la lógica de negocio
│   │   ├── services/ 
│   ├── App.jsx         # Componente principal de la app
│   └── main.jsx        # Punto de entrada del proyecto
├── .gitignore          # Archivos a ignorar por Git
├── package.json        # Configuración del proyecto y dependencias
├── vite.config.js      # Configuración de Vite
└── README.txt          # Documentación del proyecto
```

### Descripción de Carpetas

components/: Contiene los componentes presentacionales (es decir, los que se renderizan en la pantalla) que son reutilizables a lo largo de la aplicación (por ejemplo, botones, tablas, listas que se pueden usar en diferentes partes de la pagina).

containers/: Contiene los containers, que son responsables de manejar la lógica de negocio. Cada container tiene su propia carpeta de componentes presentacionales, que solo son usados en ese container.

services/: Contiene código para lógica externa a la app, como la conexión a APIs. La idea es centralizar el acceso a servicios externos para que sea fácil de mantener y reutilizar.

## Contribuciones

IMPORTANTE: Para contribuir al proyecto, por favor sigue estos pasos:

1. Crea una nueva rama con tu característica/funcionalidad
```bash
git branch NuevaFuncionalidad-branch
```

2. Asegurate de estar dentro de la rama
```bash
git checkout NuevaFuncionalidad-branch
```

3. Realiza los cambios y haz commit (tantos como quieras)
```bash
git commit -m 'Añadir nueva funcionalidad'
```

4. Envía tu rama al repositorio
```bash
git push NuevaFuncionalidad-branch
```

5. La rama entrará en revisión y deberá pasar tests. Una vez testeada se hará un merge con la branch 'dev'
``` bash
git checkout dev
git merge NuevaFuncionalidad
git branch -d NuevaFuncionalidad # Eliminar la rama
```

## Convenciones

### Con respecto a Git

1. Nombres de las ramas (branchs): nombre_de_la_rama
2. Nombres de los commit (git commit -m "_"): SCRUM-00 Funcionalidad que se agrega + Otra funcionalidad

### Con respecto a los archivos

En ingles

1. Componentes: FuncionComponente.jsx (CreateGameButton.jsx)
2. Container:   FuncionContainer.jsx (CreateGameContainer.jsx)
3. Servicios:   metodoServicio.js (postGameService.js, getGamesListService.js)

