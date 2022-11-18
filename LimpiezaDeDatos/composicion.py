import pandas as pd
import random
import time

# Extraer datos de muebles y influencers:
df1 = pd.read_csv('../DatosLimpios/muebles.csv', usecols=["item_id", "category"])
df2 = pd.read_csv('../DatosLimpios/influencer.csv', usecols=["influencer_id"])
influencer_id = df2["influencer_id"].tolist()
#print(df1, df2)

'''listaMuebles = df1["item_id"].tolist()
#print(listaMuebles)
listaCatTodos = df1["category"].tolist() 
listaCat = list()
for x in listaCatTodos:
    if x not in listaCat:
        listaCat.append(x)
#print(listaCat)'''

# Crear dataframe listrando los muebles por categoría:
df3 = df1.groupby('category')['item_id'].apply(list)
#print(df3)

# Crear diccionario de muebles por categoría:
dictCat = df3.to_dict()
#print(dictCat)

# Crear composicion_id:
compLista = list()
for x in range(1,601):
    compLista.append(x)
#print(compLista)

# crear nuevos dicts que solo llevan min-max elementos en lista como valor:
# crear lista de tuplas (tupla: ([listamuebles], "cat"))
pairs = [(v, k) for (k, v) in dictCat.items()]
#print(pairs)

# Crear Dictionario con categorías como clave y lista de varias elementos aleatorios (cantidad tb aleatoria)
#listaCSV = list()
minItems = 3
maxItems = 5
dictCom = dict()
#for tupla in pairs:
    #dictCom[tupla[1]] = [random.sample(tupla[0], random.choice(range(minItems, maxItems+1)))]
    #listaCSV = [random.choice(tupla), random.sample(tupla[0], random.choice(range(minItems, maxItems+1)))]
#print(dictCom)
    
#listaCSV = [random.choice(pairs[random.choic]), random.sample(tupla[0], random.choice(range(minItems, maxItems+1)))]

# Crear lista aleatoria que lleva: categoria y sus elementos
while True:
    randomTupla = random.choice(pairs)
    listaCSV = [id(randomTupla), random.choice(influencer_id), random.sample(randomTupla[0], random.choice(range(minItems, maxItems+1)))]
    print(listaCSV)

## hasta aqui bien
    with open(../DatosLimpios/composicion.csv, mode, encoding='UTF8') as f:
        w = csv.DictWriter(f, datos.keys())
        # If file doesn't exist, create header
        if f.tell() == 0:
            w.writeheader()

        # write the data
        w.writerow(datos)
    time.sleep(5)

