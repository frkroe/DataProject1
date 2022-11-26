# columnas: id_venta, id_cliente, composicion_id (que esta relacionado con id_influencer, id_item), cantidad, fecha


#PASOS QUE HACER

# 1. conectar con base de datos
# 2. Extraer los datos (id_cliente, id_composicion) de las tablas cliente y composicion de la base de datos

## dataframe de id_cliente --> crear lista de id_cliente: df.tolist()
## dataframe de id_composicion: crear dict de id_comp: listaComp = [[comp_id, influencer_id, [lista_items]], ...]

# 1. selecionar random lista[random lista] --> guardarlo como variable (comp. elegida)
# 2. selecionar random cantidad lista(item_ids): random.choice(listaitems) --> guardarlo como lista
