def influencer():
    #importaciones
    import pandas as pd

    #leemos los datos
    df_influencer = pd.read_csv('../rawdata/instagrammers.csv')
    #print(df_influencer)

    #añadimos influencer_id
    idList = list()
    for i in range(1,1+len(df_influencer["Username"])):
        idList.append(i)
    df_influencer["influencer_id"] = idList
    #print(df_influencer)

    #creamos pesos y la suma cumulativa para calcular la comisión
    df_influencer["weights"] = df_influencer["Likes Avg."]*0.6 + df_influencer["Followers"]*0.4
    df_influencer = df_influencer.sort_values(by="weights", ascending=True)
    df_influencer["cumSum"] = df_influencer["weights"].cumsum()/df_influencer["weights"].sum()*100

    #calculamos la comisión
    lista = list()
    for fila in df_influencer["cumSum"]:
        if fila < 25:
            lista.append(0.1)
        elif fila >= 25 and fila < 50:
            lista.append(0.2)
        elif fila >= 50 and fila < 75:
            lista.append(0.3)
        else:
            lista.append(0.5)
    df_influencer["Commission"] = lista
    #print(df_influencer)     

    #limpiamos el dataframe (extraemos las columnas)
    df_influencer = df_influencer.loc[:,["influencer_id", "Username", "Followers", "Likes Avg.", "Commission"]]
    #print(df_influencer)
    return df_influencer