def compMueble(df_muebles, numCompCat, minItems, maxItems):
    import pandas as pd
    import random
    #import os

    # Reemplaza los valores de tipo str por valores int(item_id)
    df =  pd.read_csv('../DatosLimpios/muebles/muebles.csv')
    n = len(df['item_id'])
    for i in range(n):
        a = df['item_id'][i]
        b = int(a)
        df.replace({a : b})

    # Extraer datos de muebles y composicion:
        #### aniadir csv de categoria_id
    df_compCat = df_muebles.groupby('category')['item_id'].apply(list).reset_index(name='list_items')
    #print(df_compCat)

    #df_muebles = pd.read_csv('../DatosLimpios/muebles.csv', usecols=["item_id", "category"])
    #df_composicion = pd.read_csv('../DatosLimpios/composicion.csv', usecols=["composicion_id"])

    # Crear [numCompCat] composiciones por cada categoría (crear su id, y lista de muebles [min-max] aleatoria guardando en un dict):
    #numCompCat = 10
    #minItems = 3
    #maxItems = 5
    dictCompListaItems = dict()
    global listaCompId
    listaCompId = list()
    for x in range(numCompCat+1):
        for i in range(len(df_compCat)):
            comp = str(f"comp_{x+1}_{i+1}")
            listaCompId.append(comp)
            #cat = df_compCat.iloc [i, 0]
            valor = random.sample(df_compCat.iloc[i, 1], random.randrange(minItems, maxItems+1))
            dictCompListaItems[comp] = valor
    #print(dictCompListaItems)

    # crear dataframe con un valor por cada celda (iterando por la lista de items):
    df_compMueble = pd.DataFrame(columns= ["composicion_id", "item_id"])
    for  k, v in dictCompListaItems.items():
        for i in enumerate(v):
            df_compMueble = df_compMueble.append({"composicion_id": k, "item_id":i[1]}, ignore_index=True)
    #print(df_compMueble)
    # Crear csv para probar crear dashboards in Tableau
    #os.makedirs('DatosLimpios', exist_ok=True)  
    #df_compMueble.to_csv('DatosLimpios/comp_muebles.csv', index=False)   
    return df_compMueble