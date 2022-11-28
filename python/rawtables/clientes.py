def clientes(n):
    #importaciones
    import requests
    import csv
    import random
    import pandas as pd

    #creamos una lista de ciudades
    with open("rawdata/cities.txt") as f:
        listCities = f.read().splitlines()
    #print(*listCities)

    #creamos un dataframe que añade datos a través de la API por fila en un bucle
    df_clientes = pd.DataFrame(columns= ["customer_id", "customer_name", "gender", "age", "city"])
    for i in range(n):
        URL = "https://randomuser.me/api/"
        #connectamos a la API un par de veces para evitar errores (freezing problem)
        try:
            respuesta = requests.get(URL,timeout=3)
        except requests.exceptions.Timeout as err:
            print(err)
        if respuesta.status_code >= 200 and respuesta.status_code < 300:
            #extraemos los datos en formato json
            datosjson = respuesta.json()
            row = [id(i), datosjson["results"][0]["name"]["first"], datosjson["results"][0]["gender"], datosjson["results"][0]["dob"]["age"], random.choice(listCities)]
            df_clientes.loc[i] = row
        #tambien guardamos los datos en csv por cada fila
            with open('results/clientes.csv', 'a', newline='', encoding='UTF8') as csv_file:  
                writer = csv.writer(csv_file)
                if csv_file.tell() == 0:
                    writer.writerow(["customer_id", "customer_name", "gender", "age", "city"])
                writer.writerow(row)
    #print(df_clientes)
    return df_clientes