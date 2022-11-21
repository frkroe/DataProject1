# crear dataset de clientes
import requests
import time
import random
import csv

# función para crear csv
def writeData(path, mode, datos):
    with open(path, mode, encoding='UTF8') as f:
        w = csv.DictWriter(f, datos.keys())
        
        # If file doesn't exist, create header
        if f.tell() == 0:
            w.writeheader()

        # write the data
        w.writerow(datos)
# crear lista de ciudades
with open("../Datos/cities.txt") as f:
    listCities = f.read().splitlines()
#print(*listCities)

# crear csv de clientes
with open('../DatosLimpios/clientes.csv', 'a', newline='', encoding='UTF8') as f:
    headerKey = ["cliente_id", "name", "gender", "age", "city"]
    w = csv.DictWriter(f, headerKey)
    w.writeheader()

n = int(input("Dime el número de clientes: "))
for i in range(n):
    URL = "https://randomuser.me/api/"
    # Trying several times to connect to the API to avoid a freezing problem that occurs every now and then.
    try:
        respuesta = requests.get(URL,timeout=3)
    except requests.exceptions.Timeout as err:
        print(err)
        time.sleep(1)
      
    if respuesta.status_code >= 200 and respuesta.status_code < 300:
        # Extract data in json format
        datosjson = respuesta.json()
        datos = {"cliente_id":id(datosjson), "name":datosjson["results"][0]["name"]["first"], "gender": datosjson["results"][0]["gender"], "age":datosjson["results"][0]["dob"]["age"], "city": random.choice(listCities)}
        #print(datos)
        
      # de momento, guardalos en csv:
        with open('../DatosLimpios/clientes.csv', 'a', newline='', encoding='UTF8') as f:
            w = csv.DictWriter(f, datos.keys())
            w.writerow(datos)
