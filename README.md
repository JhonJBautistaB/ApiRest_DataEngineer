![python](https://img.shields.io/badge/3.8-Python-FFD43B?style=for-the-badge&logo=python&logoColor=white) ![pandas](https://img.shields.io/badge/1.4-Pandas-306998?style=for-the-badge&logo=pandas&logoColor=white) ![SQLite3](https://img.shields.io/badge/3-SQLite-4B8BBE?style=for-the-badge&logo=sqlite&logoColor=white)

# ABOUT THE PROJECT

Este repositorio fue creado con el fin de realizar practicas de extracción de datos desde la siguiente REST API <https://restcountries.com/>

Se obtiene un pequeño set de datos simulando una tabla

| region | city   | languages                                | time |
|--------|--------|------------------------------------------|------|
| África | Angola | AF4F4762F9BD3FOF4A10CAF5B6E63DC4CE543724 | 0.23 |


## Prerequisites
Una vez que se es clonado el repositorio es necesario:
* Clonar Repositorio
 * Instalación de pip
 ```sh
  python3 -m pip install --upgrade pip 
  ```
 * Instalación de virtualenv
 ```sh
  pip install virtualenv
  ```
Crear el entorno virtual con el siguiente comando
```sh
python3 -p python3 .venv
```
## Getting Started
para poder ejecutar el código correctamente y generar el set de datos que se guarda en un archivo data.json y una tabla en html5 donde se muestra la información procesada, es necesario realizar los siguientes pasos:
 * Activar el entorno virtual
 ```sh
 source .venv/bin/activate
 ```
* instalar los paquetes dependientes
```sh
pip install -r requirements.txt
```
* inicializar las tablas de la BD
```sh
python3 init_db.py
```

## Delete a file

En la carpeta `data` del proyecto se esta guardando la información del archivo `data.json` y en `tabla.html` se presenta el set de datos seleccionado, cada vez se se ejecuta la app, la información es reemplazada y es generado un nuevo set de datos. Si deseas ver la generación de los archivos puedes borrarla sin problemas


## Diagrams

Este diagrama nos permite conocer de manera gráfica como se interconecta las APP para estraer la data y procesarla:

```mermaid
sequenceDiagram
restcountries.com ->> AppPython: request: GET:https://restcountries.com/v3.1/region/Africa
AppPython-->>SQLite: Insert: Data