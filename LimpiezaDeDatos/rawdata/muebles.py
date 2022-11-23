
def muebles():
    # Importaciones
    import pandas as pd
    #import os  

    # Leer los datos
    df = pd.read_csv('../Datos/productos.csv', index_col=[0])
    #print(df)

    # Extraer columnas y Limpiar filas: que solo se vendan online
    extractCol = df[["item_id", "name", "category", "price", "sellable_online", "link"]]
    extractRow = extractCol[extractCol["sellable_online"]== True]
    df_muebles = extractRow[["item_id", "name", "category", "price", "link"]]
    #print(muebles)
    # Crear csv's en un nuevo directorio
    #os.makedirs('../DatosLimpios', exist_ok=True)  
    #muebles.to_csv('../DatosLimpios/muebles.csv')  
    return df_muebles