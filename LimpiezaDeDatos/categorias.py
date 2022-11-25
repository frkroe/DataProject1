def categorias():
    import pandas as pd
    import uuid

    # Crea un csv(cat_muebles.csv) que combina los datos originales de los muebles(muebles2.csv) con un cat_id(muebles.csv)
    items = pd.read_csv('../DatosLimpios/muebles/muebles.csv', index_col=0).to_dict()
    key, value = "cat_id", []
    items[key] = value

    id = str(uuid.uuid1())
    for i in items['category']:
        cat = items['category'][i][:6]+id
        items['cat_id'].append(cat)

    categ_id = pd.DataFrame(items['cat_id'], columns = ["cat_id"])
    categ_id.to_csv('../DatosLimpios/muebles/muebles2.csv')

    a = pd.read_csv("../DatosLimpios/muebles/muebles.csv")
    b = pd.read_csv("../DatosLimpios/muebles/muebles2.csv")
    b = b.dropna(axis=1)
    merged = a.merge(b)
    merged.to_csv("../DatosLimpios/cat_cmuebles.csv",index=False)

categorias()