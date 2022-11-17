import pandas as pd
import random

# Extraer datos de muebles y influencers:
df1 = pd.read_csv('../DatosLimpios/muebles.csv', usecols=["item_id", "category"])
df2 = pd.read_csv('../DatosLimpios/influencer.csv', usecols=["influencer_id"])
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

# crear nuevos dicts que solo llevan 3/4/5 elementos en lista como valor; 17 categorías: 

# Crear lista con "num" valores --> serán las claves del dictParte
## num = el número de composiciones de cada categoría
listaClave = list()
num = 12
for cat, lista in dictCat.items():
    listaClave.extend([cat for i in range(num)])
#print(len(listaClave))

# Crear num*17 listas que llevan 3/4/5 elementos=item_ids --> crear una lista de estas listas
listaItems = list()
list = list()

# Dict de composiones solo con claves sin valores
dictComp = dict()
dictComp.fromkeys(listaClave)
print(dictComp)

for clave, valor in dictCat.items():
    dictComp[clave]= list.extend([random.sample(valor, 3) for i in range(num)])
print(dictComp)
'''for elemento in dictCat["Children's furniture"]:
    dict["Children's furniture"]= list.extend([random.choice(elemento, 3) for i in range(num)]) 
print(dict)'''

"""for cat in dictCat.items():
    for i in range(num):
        for lista in cat:
            list.extend([random.sample(lista, 3)]) 
            listaItems.append(list)
print(listaItems)"""
#print(dictCat["Children's furniture"])
"""
for cat, list in dictCat:
    listComp = random.sample(list, 3)
    """

