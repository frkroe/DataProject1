def ventas(v, df_muebles, df_clientes, minq, maxq):
    # Importaciones
    import pandas as pd
    import random
    import time
    from datetime import datetime
    #from main import v

    # Leer cliente_id y item_id de sus archivos y guardarlos como listas
    list_muebleId = df_muebles["item_id"].to_list()
    list_clienteId = df_clientes["cliente_id"].to_list()
    #print(list_clienteId,list_muebleId)

    # Difinir el número de ventas y las quantitdades aleatoriamente (entre min-max):
    #minq = 1
    #maxq = 5

    # Crear dataframe con nuevos ventas cada segundo
    df_ventas = pd.DataFrame()
    for i in range(v):
        fila = {"sales_id": id(i),"cliente_id":random.choice(list_clienteId), "item_id":random.choice(list_muebleId), "date": datetime.now(), "quantity": random.randrange(minq, maxq+1)}
        df_ventas = df_ventas.append(fila, ignore_index=True)
        time.sleep(1)
    #print(df_ventas)
    return df_ventas