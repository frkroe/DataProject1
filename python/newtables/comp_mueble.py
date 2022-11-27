def compMueble(df_muebles, numCompCat, minItems, maxItems):
    import pandas as pd
    import random

    #extraemos datos grupados de muebles por composicion
    df_compCat = df_muebles.groupby('category_id')['item_id'].apply(list).reset_index(name='list_items')
    #print(df_compCat)

    #creamos [numCompCat] composiciones por cada categoría (tb creando su id, y lista de muebles [min-max] aleatoria guardados en un dict)
    dictCompListaItems = dict()
    global listaCompId
    listaCompId = list()
    for x in range(numCompCat+1):
        for i in range(len(df_compCat)):
            comp = int(f"00{x+1}00{i+1}")
            listaCompId.append(comp)
            #cat = df_compCat.iloc [i, 0]
            valor = random.sample(df_compCat.iloc[i, 1], random.randrange(minItems, maxItems+1))
            valor = [int(x) for x in valor]
            dictCompListaItems[comp] = valor
    #print(dictCompListaItems)

    #creamos dataframe con un valor por cada celda (iterando por la lista de items)
    df_compMueble = pd.DataFrame(columns= ["composicion_id", "item_id"])
    for i, (k, v) in enumerate(dictCompListaItems.items()):
        for e in enumerate(v):
            df_compMueble.loc[i] = [k, e[1]]
    #print(df_compMueble)
    return df_compMueble