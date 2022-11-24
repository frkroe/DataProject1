
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
    os.makedirs('../DatosLimpios', exist_ok=True)  
    muebles.to_csv('../DatosLimpios/muebles.csv')  

    items = pd.read_csv('../DatosLimpios/muebles.csv', index_col=0).to_dict()
    key, value = "cat_id", []
    items[key] = value

    id = str(uuid.uuid1())
    for i in items['category']:
        cat = items['category'][i][:6]+id
        items['cat_id'].append(cat)

    categ_id = pd.DataFrame(items['cat_id'], columns = ["cat_id"])
    categ_id.to_csv('../DatosLimpios/muebles2.csv')

    a = pd.read_csv("../DatosLimpios/muebles.csv")
    b = pd.read_csv("../DatosLimpios/muebles2.csv")
    b = b.dropna(axis=1)
    merged = a.merge(b)
    merged.to_csv("../DatosLimpios/cat_muebles.csv",index=False)

muebles()