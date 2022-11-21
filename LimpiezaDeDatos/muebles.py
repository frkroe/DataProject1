
def muebles():
    # Importaciones
    import pandas as pd
    import os  

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

    df2 = df2.replace("category", "cat_id")
    df2 = df2.replace("Bar furniture", "001barf")
    df2 = df2.replace("Beds", "002beds")
    df2 = df2.replace("Bookcases & shelving units", "003book")
    df2 = df2.replace("Cabinets & cupboards", "004cabi")
    df2 = df2.replace("Café furniture", "005café")
    df2 = df2.replace("Chairs", "006chai")
    df2 = df2.replace("Chests of srawers & drawer units", "007ches")
    df2 = df2.replace("Childrens furniture", "008chil")
    df2 = df2.replace("Nursery furniture", "009nurs")
    df2 = df2.replace("Outdoor furniture", "010outd")
    df2 = df2.replace("Room dividers", "011room")
    df2 = df2.replace("Sideboards, buffets & console tables", "012side")
    df2 = df2.replace("Sofas & armchairs", "013sofa")
    df2 = df2.replace("Tables & desks", "014tabl")
    df2 = df2.replace("Trolleys", "015trol")
    df2 = df2.replace("Tv & media furniture", "016tvme")
    df2 = df2.replace("Wardrobes", "017ward")


muebles()