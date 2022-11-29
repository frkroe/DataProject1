# Importaciones
from rawtables.muebles import muebles
from rawtables.influencers import influencer
from rawtables.clientes import clientes
from newtables.composicion import composicion
from newtables.comp_mueble import compMueble
from newtables.ventas import ventas
import os
from tablas.alimentar_tablas import alimentar

'''print("""
***********************************
Bienvenidos a nuestro Data Project!
Para poder enseñarte cosas chulas, necesitamos que rellenes los campos siguientes:
""")'''

n = 500
v = 1000
numCompCat = 3
minItems = 2
maxItems = 5
minq = 1
maxq = 3
x = 1

'''
print("""
***********************************
Bienvenidos a nuestro Data Project!
Para poder enseñarte cosas chulas, necesitamos que rellenes los campos siguientes:""")
n = int(input("Dime el número de clientes: "))
v = int(input("Dime el número de ventas: "))
numCompCat = int(input("Dime el número de composiciones por cada categoría: "))
minItems = int(input("Dime la cantidad mínima de productos que tiene que salir en una composición: "))
maxItems = int(input("Dime la cantidad máxima de productos que tiene que salir en una composición: "))
minq = int(input("Dime la cantidad mínima de un producto comprado: "))
maxq = int(input("Dime la cantidad máxima de  un producto comprado: "))
x = int(input("Dime cuantos segundos hay que esperar entre cada venta: "))'''


#Creamos un nuevo directorio results
if not os.path.isdir("results/"):
        os.mkdir("results/")

# Dataframes estáticos: 
# los creamos y exportamos como csv's
df_muebles, df_category = muebles()
df_influencer = influencer()
df_compMueble = compMueble(df_muebles, numCompCat, minItems, maxItems)
df_composicion = composicion(df_influencer)
#csv's en  el directorio results
df_influencer.to_csv('results/influencer.csv', index=False)
df_muebles.to_csv('results/muebles.csv', index=False)  
df_category.to_csv('results/category.csv', index=False)  
df_compMueble.to_csv('results/comp_muebles.csv', index=False)  
df_composicion.to_csv('results/composicion.csv', index=False)

# Dataframes "dinámicos" (en bucle)
# Ojo: df_clientes y df_ventas se crea dinámicamente, por lo tanto se crea los csv's en sus archivos 
df_clientes = clientes(n)
df_ventas = ventas(v, df_compMueble, df_clientes, minq, maxq, x)

#alimentamos las tablas en postgres con los datos creados en los csv's
alimentar()

#comprobamos los dataframes
'''print(f"""
{df_muebles}
************
{df_category}
************
{df_influencer}
************
{df_clientes}
************
{df_compMueble}
************
{df_composicion}
************
{df_ventas}
""")'''

#comprobamos los tipos de datos
'''print(f"""
{df_muebles.dtypes}
************
{df_category.dtypes}
************
{df_influencer.dtypes}
************
{df_clientes.dtypes}
************
{df_compMueble.dtypes}
************
{df_composicion.dtypes}
************
{df_ventas.dtypes}
""")'''