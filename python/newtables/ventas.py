def ventas(v, df_compMueble, df_clientes, minq, maxq, x):
    # Importaciones
    import pandas as pd
    import csv
    import random
    import time
    from datetime import datetime

    #leemos los customer_id de su archivo y los guardamos como lista
    list_clienteId = df_clientes["customer_id"].to_list()
    #print(list_clienteId,list_muebleId)

    #creamos dataframe con nuevos ventas cada 1 segundo
    df_ventas = pd.DataFrame(columns= ["sales_id", "customer_id", "product_id", "composition_id", "date", "quantity"])
    for i in range(v):
        randomrow = df_compMueble.sample()
        row = [id(i), random.choice(list_clienteId), randomrow["product_id"].to_list()[0], randomrow["composition_id"].to_list()[0], datetime.now(),  random.randrange(minq, maxq+1)]
        df_ventas.loc[i] = row
    #print(df_ventas)
    #tambien guardamos los datos en csv por cada fila
        with open('results/ventas.csv', 'a', newline='', encoding='UTF8') as csv_file:  
                writer = csv.writer(csv_file)
                if csv_file.tell() == 0:
                    writer.writerow(["sales_id", "customer_id", "product_id", "composition_id", "date", "quantity"])
                writer.writerow(row)
        time.sleep(x)
    return df_ventas