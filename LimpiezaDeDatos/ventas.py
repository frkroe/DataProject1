def ventas():
    # Importaciones
    from rawdata.clientes import clientes
    from rawdata.muebles import muebles
    import pandas as pd
    import random
    import time
    from datetime import datetime

    list_clienteId = clientes()["cliente_id"].to_list()
    list_muebleId = muebles()["item_id"].to_list()
    #print(list_clienteId,list_muebleId)

    n = int(input("Dime el número de ventas: "))
    minq = 1
    maxq = 5
    df_ventas = pd.DataFrame()
    for i in range(n+1):
        fila = {"sales_id": id(i),"cliente_id":random.choice(list_clienteId), "item_id":random.choice(list_muebleId), "date": datetime.now(), "quantity": random.randrange(minq, maxq+1)}
        df_ventas = df_ventas.append(fila, ignore_index=True)
        time.sleep(2)
    #print(df_ventas)