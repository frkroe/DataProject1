# DataProject1

## Introducción
El caso de uso que vamos a trabajar en este Dataproject es que Ikea ha solicitado a EDEM ayuda para formalizar una nueva línea de negocio dentro de su tienda.
La idea de esta línea es monetizar la socialización de sus productos, para ello quieren crear un sistema de recomendación para su influencers.
Los influencers podrán subir imagenes de sus composiciones de productos, pudiendo ser estas compradas por clientes generándoles a los influencers un pago por su         colaboración.

## Datos
Fuentes:
- [Productos de IKEA](https://www.kaggle.com/datasets/ahmedkallam/ikea-sa-furniture-web-scraping)
- [API para los clientes](https://randomuser.me/api)
- [Ciudades de Arabia Saudita](https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Saudi_Arabia)
- [Top 200 Influencers](https://www.kaggle.com/datasets/syedjaferk/top-200-instagrammers-data-cleaned?select=top_200_instagrammers.csv)


## Pasos
1. Origen del problema: 
  - analizar el caso y evaluar los pasos a seguir en función de los requerimientos solicitados.
2. Ingestionar datos: 
  - extraer y limpiar los datos de csv: influencers y muebles.
  - crear dataset de clientes: a través de la api [randomuser.me](https://randomuser.me), añadiendo la ciudad a través de un .txt de manera aleatoria.
3. Procesamaiento de datos:
  - crear las comisiones de los influencers a través de una fórmula de ponderación donde tenemos en cuenta el nº followers y likes de cada influencer
      de manera que creamos 4 rangos que oscilan desde el 1% al 5%.
  - crear aleatoriamnerte los archivos de composiciones, categorías, muebles_composición y ventas.
4. Almacenamiento de datos:
  - conectar de forma automática PostgreSQL creando la base de datos y las tablas, las cuales alimentamos a través de la ejecución del docker-compose.
6. Visualizacion datos:
  - mostrar en varios dashboards de Tableau los datos de ventas, clientes e influencers por distintas categorías y características.

## Setup
1. Levantar el contenedor: docker-compose up -d
  - Una vez levantado el docker se crean 3 contenedores:
       - postgres
       - pgadmin
       - srv-python
   - Automaticamente se crea la base de datos **ikea2022** en PostgreSQL y se ejecuta el archivo main.py el cual crea las tablas de dicha base de datos y las    alimenta de forma automatica
 2. Entrar en [pgAdmin](http://localhost:5050/browser) introduciendo:
   - User: pgadmin4@pgadmin.org
   - Password: admin
 3. Crear el servidor de postgres introduciendo:
   - Name: el que nosotros queramos
   - Host name/address: postgres
   - Port: 5432
   - Maintenance database: postgres
   - Username: postgres
   - Password: ikea2022
  4. Conectar Tableau a traves de la conexion a un servidor PostgreSQL introduciendo:
   - Servidor: localhost
   - Port: 5432
   - Base de dato: ikea2022
   - Nombre de usuario: postgres
   - Contraseña: ikea2022
   - Requiere SSL: debe aparecer sin marcar
