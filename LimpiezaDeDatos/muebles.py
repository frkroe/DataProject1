
def muebles():
    # Importaciones
    import pandas as pd
    import os  
    import uuid

    # Leer los datos
    df = pd.read_csv('../Datos/productos.csv')
    #print(df)

    # Extraer columnas
    extractCol = df[["item_id", "name", "category", "price", "sellable_online", "link"]]

    # Limpiar filas: que solo se vendan online
    extractRow = extractCol[extractCol["sellable_online"]== True]
    muebles = extractRow[["item_id", "name", "category", "price", "link"]]
    #print(muebles)

    # Crear csv's en un nuevo directorio
    os.makedirs('../DatosLimpios/muebles', exist_ok=True)  
    muebles.to_csv('../DatosLimpios/muebles/muebles.csv')  

    # Reemplaza los valores de tipo str por valores int(item_id) o float(price) según el caso
    df =  pd.read_csv('../DatosLimpios/muebles/muebles.csv')
    n = len(df['item_id'])
    for i in range(n):
        a = df['item_id'][i]
        b = int(a)
        c = df['price'][i]
        d = float(c)
        df.replace({a : b, c : d})

   
muebles()
