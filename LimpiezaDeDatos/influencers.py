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
    i += 1
extractCol["influencer_id"] = idList
#print(extractCol)

# Crear pesos y la suma cumulativa para calcular la comisión:
extractCol["weights"] = extractCol["Likes Avg."]*0.6 + extractCol["Followers"]*0.4
extractCol = extractCol.sort_values(by="weights", ascending=True)
extractCol["cumSum"] = extractCol["weights"].cumsum()/extractCol["weights"].sum()*100
#print(extractCol)


def categorise(row):
    if row["cumSum"] <= 25:
        return 0.01
    elif row["CumSum"] > 25 and row["cumSum"] <= 50:
        return 0.02
    elif row["cumSum"] > 50 and row["cumSum"] <= 75:
        return 0.03
    else:
        return 0.05

extractCol["commission"] = extractCol.apply(lambda row: categorise(row), axis=1)
print(extractCol)

# Crear csv's en un nuevo directorio
#os.makedirs('../DatosLimpios', exist_ok=True)  
#extractCol.to_csv('../DatosLimpios/influencer.csv')  