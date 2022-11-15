# Importaciones
import pandas as pd
import os  




# Leer los datos
df = pd.read_csv('../Datos/instaInfluencers.csv')
#print(df)


## ESTO ESTA MAL; HAY QUE ANIADIR EL ID 
# Extraer columnas
extractCol = df[["username", "Followers", "Likes Avg."]]
extractCol['influencer_id'] = id(df)
#print(extractCol)



# Crear csv's en un nuevo directorio
os.makedirs('../DatosLimpios', exist_ok=True)  
extractCol.to_csv('../DatosLimpios/influencer.csv')  