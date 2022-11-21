# Importaciones
import pandas as pd
import os  

# Leer los datos
df = pd.read_csv('../Datos/instagrammers.csv')
#print(df)

# Extraer columnas
extractCol = df[["Username", "Followers", "Likes Avg."]]

# Añadir influencer_id
idList = list()
for i in range(1,201):
    idList.append(i)
extractCol["influencer_id"] = idList
#print(extractCol)

# Crear pesos y la suma cumulativa para calcular la comisión:
extractCol["weights"] = extractCol["Likes Avg."]*0.6 + extractCol["Followers"]*0.4
extractCol = extractCol.sort_values(by="weights", ascending=True)
extractCol["cumSum"] = extractCol["weights"].cumsum()/extractCol["weights"].sum()*100

# Calcular la comisión:
lista = list()
for fila in extractCol["cumSum"]:
    if fila < 25:
        lista.append(0.1)
    elif fila >= 25 and fila < 50:
        lista.append(0.2)
    elif fila >= 50 and fila < 75:
        lista.append(0.3)
    else:
        lista.append(0.5)
#print(lista)
extractCol["Commission"] = lista
#print(extractCol)     

# Limpir el dataframe:
influencer = extractCol[["influencer_id", "Username", "Followers", "Likes Avg.", "Commission"]]
print(influencer)
# Crear csv's en un nuevo directorio
os.makedirs('../DatosLimpios', exist_ok=True)  
influencer.to_csv('../DatosLimpios/influencer.csv', index=False)  