# Importaciones
from LimpiezaDeDatos.rawdata.muebles import muebles
from LimpiezaDeDatos.rawdata.influencers import influencer
from LimpiezaDeDatos.rawdata.clientes import clientes
from LimpiezaDeDatos.composicion import composicion
from LimpiezaDeDatos.comp_mueble import compMueble
from LimpiezaDeDatos.ventas import ventas

print("""
***********************************
Bienvenidos a nuestro Data Project!
Para poder enseñarte cosas chulas, necesitamos que rellenes los campos siguientes:
""")
n = int(input("Dime el número de clientes: "))
v = int(input("Dime el número de ventas: "))
numCompCat = int(input("Dime el número de composiciones por cada categoría: "))
minItems = int(input("Dime la cantidad mínima de productos que tiene que salir en una composición: "))
maxItems = int(input("Dime la cantidad máxima de productos que tiene que salir en una composición: "))
minq = int(input("Dime la cantidad mínima de un producto comprado: "))
maxq = int(input("Dime la cantidad máxima de  un producto comprado: "))


# Dataframes
df_muebles = muebles()
df_influencer = influencer()
df_clientes = clientes(n)
df_compMueble = compMueble(df_muebles, numCompCat, minItems, maxItems)
df_composicion = composicion(df_influencer)
df_ventas = ventas(v, df_muebles, df_clientes, minq, maxq)

print(f"""
{df_muebles}
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
""")