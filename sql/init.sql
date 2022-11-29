CREATE TABLE IF NOT EXISTS clientes(
        customer_id BIGINT NOT NULL,
        customer_name TEXT NOT NULL,
        gender TEXT NOT NULL,
        age INT NOT NULL,
        city TEXT NOT NULL, 
        CONSTRAINT PK_clientes PRIMARY KEY (customer_id));

CREATE TABLE IF NOT EXISTS influencers(
        influencer_id INT NOT NULL,
        influencer_name TEXT NOT NULL,
        commission NUMERIC(3, 2)NOT NULL, 
        CONSTRAINT PK_influencers PRIMARY KEY (influencer_id));

CREATE TABLE IF NOT EXISTS categoria(
        category_id INT NOT NULL,
        category_name TEXT NOT NULL, 
        CONSTRAINT PK_categoria PRIMARY KEY (category_id));

CREATE TABLE IF NOT EXISTS composicion(
        composition_id INT NOT NULL,
        influencer_id INT NOT NULL, 
        CONSTRAINT PK_composicion PRIMARY KEY (composition_id), 
        CONSTRAINT FK_composicion FOREIGN KEY (influencer_id) REFERENCES influencers(influencer_id));

CREATE TABLE IF NOT EXISTS mueble_composicion (
        composition_id INT NOT NULL,
        product_id INT NOT NULL, 
        CONSTRAINT PK_mueble_composicion PRIMARY KEY (composition_id, product_id));

CREATE TABLE IF NOT EXISTS muebles (
        product_id INT NOT NULL,
        product_name TEXT NOT NULL,
        category_id INT NOT NULL,
        price NUMERIC(5, 1) NOT NULL,
        link TEXT NOT NULL, 
        CONSTRAINT PK_muebles PRIMARY KEY (product_id),
        CONSTRAINT FK_muebles FOREIGN KEY (category_id) REFERENCES categoria(category_id));

CREATE TABLE IF NOT EXISTS ventas (
        sales_id BIGINT NOT NULL,
        customer_id BIGINT REFERENCES clientes(customer_id) NOT NULL,
        product_id INT NOT NULL,
        composition_id INT REFERENCES composicion(composition_id) NOT NULL,
        date TIMESTAMP NOT NULL,
        quantity INT NOT NULL,
        CONSTRAINT PK_ventas PRIMARY KEY (sales_id));