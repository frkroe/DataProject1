def composicion(df_influencer):
    from LimpiezaDeDatos.comp_mueble import listaCompId
    import pandas as pd
    import random
    #import os

    # Extraer datos de influencers:
    #df = pd.read_csv('../DatosLimpios/influencer.csv', usecols=["influencer_id"])
    influencer_id = df_influencer["influencer_id"].tolist()

    # Elegir aleatoriamente x influencers:
    listaInfl = list()
    for i in range(1, len(listaCompId)+1):
        listaInfl.append(random.choice(influencer_id))
    #print(listaInfl)

    # Crear dataframe
    df_composicion = pd.DataFrame(zip(listaCompId, listaInfl), columns =["composicion_id", "influencer_id"])
    #print(df_composicion)
    # Crear csv para probar crear dashboards in Tableau
    #os.makedirs('../DatosLimpios', exist_ok=True)  
    #df_composicion.to_csv('../DatosLimpios/composicion.csv', index=False)  
    return df_composicion