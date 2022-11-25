def categorias():
    import pandas as pd
    import uuid
    import csv

    # Crea un csv(cat_id.csv) a partir del csv muebles
    
    items = pd.read_csv('../DatosLimpios/muebles/muebles.csv', index_col=0).to_dict()
    key, value = "cat_id", []
    items[key] = value

    id = str(uuid.uuid1())
    with open("../DatosLimpios/muebles/cat_id.csv", "w") as result:
        writer = csv.writer(result)
        writer.writerow(('category','cat_id'))
        for i in items['category']:
            cat = items['category'][i][:6]+id
            writer.writerow((items['category'][i],cat))
categorias()