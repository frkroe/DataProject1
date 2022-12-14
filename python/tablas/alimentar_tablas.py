def alimentar():
    import psycopg2
    import csv
    while True: 
        try: 
            #realizamos la conexion al servidor de localhost y la base de datos ikea en postgres
            connection = psycopg2.connect(host="postgres", dbname="ikea2022", user="postgres", password="ikea2022")
            #definimos un objeto de acceso a datos
            mycursor = connection.cursor()
            break
        except(Exception, psycopg2.Error) as error:
                print('Unable to connect', error)

    #definimos la funcion que alimenta la tabla clientes
    with open('results/clientes.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            # Preparamos la query de SQL query para insertar dattos en la base de datos
            sql = "INSERT INTO clientes (customer_id, customer_name, gender, age, city) VALUES ('%s', '%s', '%s', '%s', '%s');" % (row[0], row[1], row[2], row[3], row[4])
            print(sql)
            try:
                #Ejecutamos el comando SQL
                mycursor.execute(sql)
                #Commit de nuestros cambios en la base de datos
                connection.commit()
                #comprobamos con un print si se ejecuta correctamente
                #print("OK_clientes")
            except:
                # Rollback en caso de que haya un error
                connection.rollback()
                #comprobamos con un print si da fallo
                #print("Fallo_clientes")

    #definimos la funcion que alimenta la tabla influencers
    with open('results/influencer.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            sql = "INSERT INTO influencers (influencer_id, influencer_name, commission) VALUES ('%s', '%s', '%s');" % (row[0], row[1], row[2])
            print(sql)
            try:
                mycursor.execute(sql)
                connection.commit()
                #print("OK_influencers")
            except:
                connection.rollback()
                #print("Fallo_influencers")

    #definimos la funcion que alimenta la tabla categoria
    with open('results/category.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            sql = "INSERT INTO categoria (category_id, category_name) VALUES ('%s', '%s');" % (row[0], row[1])
            print(sql)
            try:
                mycursor.execute(sql)
                connection.commit()
                #print("OK")
            except:
                # Rollback in case there is any error
                connection.rollback()
                #print("Fallo")

    #definimos la funcion que alimenta la tabla composicion
    with open('results/composicion.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            sql = "INSERT INTO composicion (composition_id, influencer_id) VALUES ('%s', '%s');" % (row[0], row[1])
            print(sql)
            try:
                mycursor.execute(sql)
                connection.commit()
                #print("OK_composicion")
            except:
                connection.rollback()
                #print("Fallo_composicion")

    #definimos la funcion que alimenta la tabla mueble_composicion
    with open('results/comp_muebles.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            sql = "INSERT INTO mueble_composicion (composition_id, product_id) VALUES ('%s', '%s');" % (row[0], row[1])
            print(sql)
            try:
                mycursor.execute(sql)
                connection.commit()
                #print("OK_mueble_composicion")
            except:
                connection.rollback()
                #print("Fallo_mueble_composicion")

    #definimos la funcion que alimenta la tabla muebles
    with open('results/muebles.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            sql = "INSERT INTO muebles (product_id,product_name,category_id,price,link) VALUES ('%s', '%s','%s', '%s', '%s');" % (row[0], row[1], row[2], row[3], row[4])
            print(sql)
            try:
                mycursor.execute(sql)
                connection.commit()
                #print("OK_muebles")
            except:
                connection.rollback()
                #print("Fallo_muebles")

    #definimos la funcion que alimenta la tabla ventas

    with open('results/ventas.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            sql = "INSERT INTO ventas (sales_id,customer_id,product_id, composition_id, date, quantity) VALUES ('%s', '%s','%s','%s', '%s', '%s');" % (row[0], row[1], row[2], row[3], row[4], row[5])
            print(sql)
            try:
                mycursor.execute(sql)
                connection.commit()
                #print("OK_ventas")
            except:
                connection.rollback()
                #print("Fallo_ventas")


    #cerramos la conexion SQL
    connection.close()

if __name__ == "__main__":
    alimentar()