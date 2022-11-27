def muebles():
    #importaciones
    import pandas as pd

    #leemos los datos
    df_muebles_all = pd.read_csv('../rawdata/productos.csv', index_col=[0])
    #print(df)

    #limpiamos filas (por productos que solo se vendan online)
    df_muebles_all = df_muebles_all.loc[df_muebles_all["sellable_online"] == True]

    #creamos category_id 
    listaCat = list(set(df_muebles_all["category"].tolist()))
    for idx, e in enumerate(listaCat):
        df_muebles_all.loc[df_muebles_all["category"] == e, "category_id"] = idx+1
    df_muebles_all["category_id"]= df_muebles_all["category_id"].astype(int)

    #creamos los dataframes muebles y category solo con las columnas necesarias (extraemos columnas)
    df_muebles = df_muebles_all.loc[:, ["item_id", "name", "category_id", "price", "link"]]
    df_category = df_muebles_all.loc[:, ["category_id", "category"]].drop_duplicates().sort_values(by="category_id")
    #print(df_muebles, df_category)
    return df_muebles, df_category