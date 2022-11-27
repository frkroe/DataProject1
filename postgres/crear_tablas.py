import psycopg2

#realizamos la conexion al servidor de localhost y la base de datos ikea en postgres
conn = psycopg2.connect("host='localhost' dbname='ikea' user='postgres' password='Ikea2022'")
cursor = conn.cursor()

TABLAS = {}

#creamos la query para la tabla clientes
TABLAS['clientes'] = ( 
    "CREATE TABLE IF NOT EXISTS clientes("
    "customer_id BIGINT PRIMARY KEY NOT NULL,"
    "name TEXT NOT NULL,"
    "gender TEXT NOT NULL,"
    "age INT NOT NULL,"
    "city TEXT NOT NULL)")

#creamos la query para la tabla influencers
TABLAS['influencers'] = ( 
    "CREATE TABLE IF NOT EXISTS influencers("
    "influencer_id INT PRIMARY KEY NOT NULL,"
	"username TEXT NOT NULL,"
    "commission NUMERIC(3, 2) NOT NULL)")

#creamos la query para la tabla categoria
TABLAS['categoria'] = ( 
    "CREATE TABLE IF NOT EXISTS categoria("
    "category_id INT PRIMARY KEY NOT NULL,"
    "category_name TEXT NOT NULL)")

#creamos la query para la tabla composicion
TABLAS['composicion'] = ( 
    "CREATE TABLE IF NOT EXISTS composicion("
    "composition_id INT PRIMARY KEY NOT NULL,"
    "influencer_id INT NOT NULL,"
    "category_id TEXT NOT NULL)")

#creamos la query para la tabla mueble_composicion
TABLAS['mueble_composicion'] = ( 
"CREATE TABLE IF NOT EXISTS mueble_composicion ("
	"product_id INT PRIMARY KEY NOT NULL,"
    "composition_id INT NOT NULL)")

#creamos la query para la tabla muebles
TABLAS['muebles'] = ( 
    "CREATE TABLE IF NOT EXISTS muebles ("
    "product_id INT PRIMARY KEY NOT NULL,"
    "product_name TEXT NOT NULL,"
    "category_id INT NOT NULL,"
    "price NUMERIC(5, 1) NOT NULL,"
    "link TEXT NOT NULL)")

#creamos la query para la tabla ventas
TABLAS['ventas'] = ( 
    "CREATE TABLE IF NOT EXISTS ventas ("
    "sales_id INT PRIMARY KEY NOT NULL,"
    "date DATE NOT NULL,"
	"customer_id BIGINT NOT NULL,"
	"product_id INT NOT NULL,"
	"quantity INT NOT NULL)")

#creamos las distintas tablas
for name, ddl in TABLAS.items():
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)

conn.commit()