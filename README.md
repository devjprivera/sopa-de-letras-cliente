# sopa-de-letras-cliente
Cliente encargado de resolver sopa de letras dado un listado de palabras y una matriz de letras.

## Recursos Especiales
Se utilizó Visual Studio Code para el desarrollo de este cliente. Se debe tener en cuenta que se debe instalar la versión más reciente de Python para ejecutar el cliente.

## Tecnologías Empleadas
Para el desarrollo se utilizó Python con el framework backend FastAPI y HTML utilizando los estilos ofrecidos por Bootstrap y templating gracias a Jinja2. Las librerías utilizadas para el desarrollo de este cliente fueron: fastapi, uvicorn, jinja2 y python-multipart.

## Guía de Despliegue
El despliegue de este cliente se realiza de la siguiente forma:

1. Clonar el repositorio por medio de git clone: git clone https://github.com/devjprivera/sopa-de-letras-cliente.git.
2. Abrir consola de comandos dentro de la carpeta backend, la cual se encuentra dentro del repositorio.
3. Ejecutar en la consola de comandos lo siguiente: pip install -r requirements.txt para instalar los paquetes necesarios para el cliente. Recuerde verificar que primero exista una versión reciente de Python y este sea agregado al PATH.
4. Ejecutar el cliente de forma local con el siguiente comando: uvicorn main:app --reload.
5. Acceder al enlace http://localhost:8000/ para interactuar con el cliente.
