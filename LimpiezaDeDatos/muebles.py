# Importaciones
import pandas as pd
import os  

# Leer los datos
df = pd.read_csv('../Datos/productos.csv')
#print(df)

# Extraer columnas
extractCol = df[["item_id", "name", "category", "price", "sellable_online", "link"]]

# Limpiar filas: que solo se vendan online
extractRow = extractCol[extractCol["sellable_online"]== True]
muebles = extractRow[["item_id", "name", "category", "price", "link"]]
#print(muebles)

# Crear csv's en un nuevo directorio
os.makedirs('../DatosLimpios', exist_ok=True)  
muebles.to_csv('../DatosLimpios/muebles.csv')  