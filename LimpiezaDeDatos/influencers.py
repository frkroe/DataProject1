# Importaciones
import pandas as pd
import os  

# Leer los datos
df = pd.read_csv('../Datos/influencers.csv')
#print(df)

# Extraer columnas
extractCol = df[["Rank", "Account", "Followers", "Authentic engagement"]]
#print(extractCol)


# Renombrar el rank al influencer_id
influencer = extractCol.rename(columns={'Rank': 'influencer_id'}) 
#print(influencer)

# Crear csv's en un nuevo directorio
os.makedirs('../DatosLimpios', exist_ok=True)  
influencer.to_csv('../DatosLimpios/influencer.csv')  