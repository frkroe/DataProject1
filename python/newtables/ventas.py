def ventas(v, df_muebles, df_clientes, minq, maxq):
    # Importaciones
    import pandas as pd
    import csv
    import random
    import time
    from datetime import datetime

    #creamos csv de clientes
    with open('results/sales.csv', 'a', newline='', encoding='UTF8') as f:
        headerKey = ["sales_id","customer_id","item_id","date","quantity"]
        w = csv.DictWriter(f, headerKey)
        w.writeheader()

    #leemos customer_id y item_id de sus archivos y los guardamos como listas
    list_muebleId = df_muebles["item_id"].to_list()
    list_clienteId = df_clientes["customer_id"].to_list()
    #print(list_clienteId,list_muebleId)

    #creamos dataframe con nuevos ventas cada 1 segundo
    df_ventas = pd.DataFrame(columns= ["sales_id", "customer_id", "item_id", "date", "quantity"])
    for i in range(v):
        df_ventas.loc[i] = [id(i), random.choice(list_clienteId), random.choice(list_muebleId), datetime.now(),  random.randrange(minq, maxq+1)]
        time.sleep(1)
    #print(df_ventas)
    #tambien guardamos los datos en csv por cada fila
        with open('results/sales.csv', 'a', newline='', encoding='UTF8') as f:
            df_ventas.to_csv(f, header=False, index=False)
    return df_ventas