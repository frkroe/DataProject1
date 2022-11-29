CREATE TABLE IF NOT EXISTS clientes(
        customer_id BIGINT PRIMARY KEY NOT NULL,
        customer_name TEXT NOT NULL,
        gender TEXT NOT NULL,
        age INT NOT NULL,
        city TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS influencers(
        influencer_id INT PRIMARY KEY NOT NULL,
        influencer_name TEXT NOT NULL,
        commission NUMERIC(3, 2) NOT NULL);

CREATE TABLE IF NOT EXISTS categoria(
        category_id INT PRIMARY KEY NOT NULL,
        category_name TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS composicion(
        composition_id INT PRIMARY KEY NOT NULL,
        influencer_id INT NOT NULL);

CREATE TABLE IF NOT EXISTS mueble_composicion (
        composition_id INT NOT NULL,
        product_id INT PRIMARY KEY NOT NULL);

CREATE TABLE IF NOT EXISTS muebles (
        product_id INT PRIMARY KEY NOT NULL,
        product_name TEXT NOT NULL,
        category_id INT NOT NULL,
        price NUMERIC(5, 1) NOT NULL,
        link TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS ventas (
        sales_id BIGINT PRIMARY KEY NOT NULL,
        customer_id BIGINT NOT NULL,
        product_id INT NOT NULL,
        date TIMESTAMP NOT NULL,
        quantity INT NOT NULL);