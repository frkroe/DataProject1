def compMueble(df_muebles, numCompCat, minItems, maxItems):
    import pandas as pd
    import random

    #extraemos datos grupados de muebles por composicion
    df_compCat = df_muebles.groupby('category_id')['product_id'].apply(list).reset_index(name='list_items')
    #print(df_compCat)

    #creamos [numCompCat] composiciones por cada categoría (tb creando su id, y lista de muebles [min-max] aleatoria guardados en un dict)
    dictCompListaItems = dict()
    global listaCompId
    listaCompId = list()
    for x in range(numCompCat+1):
        for i in range(len(df_compCat)):
            comp_id = int(f"{x+1}00{i+1}")
            listaCompId.append(comp_id)
            #cat = df_compCat.iloc [i, 0]
            valor = random.sample(df_compCat.iloc[i, 1], random.randrange(minItems, maxItems+1))
            valor = [int(x) for x in valor]
            dictCompListaItems[comp_id] = valor
    #print(dictCompListaItems)

    #creamos dataframe con un valor por cada celda (iterando por la lista de items)
    df_compMueble = pd.DataFrame(columns= ["composition_id", "product_id"])
    for  k, v in dictCompListaItems.items():
        for i in enumerate(v):
            df_dictionary = pd.DataFrame([{"composition_id": k, "product_id":i[1]}])
            df_compMueble = pd.concat([df_compMueble, df_dictionary], ignore_index=True)
    #print(df_compMueble)
    return df_compMueble