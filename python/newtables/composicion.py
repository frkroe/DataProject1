def composicion(df_influencer):
    from newtables.comp_mueble import listaCompId
    import pandas as pd
    import random

    #extraemos el influencer_id (= variable global) del archivo influencers
    influencer_id = df_influencer["influencer_id"].tolist()

    #elegimos aleatoriamente los influencers (número depende del número de composiciones)
    listaInfl = list()
    for i in range(1, len(listaCompId)+1):
        listaInfl.append(random.choice(influencer_id))
    #print(listaInfl)

    #creamos el dataframe
    dict = {"composicion_id": listaCompId, "influencer_id": listaInfl}
    df_composicion = pd.DataFrame(dict)
    #print(df_composicion)
    return df_composicion