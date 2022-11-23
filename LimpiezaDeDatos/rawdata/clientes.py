def clientes():
    # Importaciones
    import requests
    import csv
    import random
    import pandas as pd

    data = []
    df_clientes = pd.DataFrame(data)

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
        if respuesta.status_code >= 200 and respuesta.status_code < 300:
            # Extract data in json format
            datosjson = respuesta.json()
            fila = {"cliente_id":id(datosjson), "name":datosjson["results"][0]["name"]["first"], "gender": datosjson["results"][0]["gender"], "age":datosjson["results"][0]["dob"]["age"], "city": random.choice(listCities)}
            df_clientes = df_clientes.append(fila, ignore_index=True)
    #print(df_clientes)
    return df_clientes
        # de momento, guardalos en csv:
        #with open('../DatosLimpios/clientes.csv', 'a', newline='', encoding='UTF8') as f:
            #w = csv.DictWriter(f, fila.keys())
            #w.writerow(fila)