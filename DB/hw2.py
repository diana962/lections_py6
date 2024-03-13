# Задание: Работа с базой данных PostgreSQL

# Цели задания:

# Проверка знаний и умений по добавлению, обновлению и заполнению данными таблиц в базе данных PostgreSQL.

# Описание задания:

# В рамках данного задания вам предстоит работать с базой данных для интернет-магазина. Вам будет необходимо создать таблицы, добавить в них данные, обновить определенные записи и выполнить ряд запросов для проверки введенной информации.

# Часть 1: Подготовка базы данных

# 1. Создайте базу данных OnlineStore`.

# 2. Внутри базы данных создайте следующие таблицы:

# Products (Товары): id (первичный ключ), пате (имя), price (цена), quantity (количество на складе).

# . Customers (Покупатели): id (первичный ключ), first_name (имя), last_name (фамилия), email (электронная почта).

# . Orders (Заказы): id (первичный ключ), customer_id (внешний ключ к таблице Customers), order_date (дата заказа), total_amount (общая сумма).

# Часть 2: Заполнение таблиц данными

# 1. Добавьте не менее пяти записей в таблицу 'Products'.

# 2. Добавьте не менее трех записей в таблицу Customers.

# 3. Создайте заказы в таблице Orders, связав их с покупателями и укажите общую сумму заказа.

# Часть 3: Обновление данных

# 1. Измените цены на некоторые товары в лице Products.

# 2. Обновите информацию о количестве товара на складе после создания заказов.


# -- Active: 1709792650783@@127.0.0.1@5432@online_store@public

# CREATE TABLE products (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(70),
#     price INTEGER CHECK(price > 0),
#     quantity INTEGER CHECK(quantity > 0)
# )

# CREATE TABLE customers(
#     id SERIAL PRIMARY KEY,
#     first_name VARCHAR(70),
#     last_name VARCHAR(100),
#     email VARCHAR(100)
# )

# CREATE TABLE orders(
#     id SERIAL PRIMARY KEY,
#     customer_id INTEGER,
#     FOREIGN KEY (customer_id) REFERENCES customers(id)
# )

# INSERT INTO customers (first_name, last_name, email) VALUES
# ('Monkey', 'Dance', 'fighter')

# INSERT INTO orders (customer_id) VALUES (1)

# ALTER TABLE orders
# ADD COLUMN order_date DATE,
# ADD COLUMN total_amount INTEGER;

# ALTER TABLE customers
# DROP COLUMN order_date,
# DROP COLUMN total_amount;


# INSERT INTO products (name, price, quantity) VALUES
# ('Apple', 10, 2), ('Pears', 22, 5), ('Mango', 50, 6), ('Peach', 66, 1), ('Banane', 30, 4)

# INSERT INTO customers (first_name, last_name, email) VALUES
# ('Tiger', 'Strip', 'tiger123'),
# ('Lion', 'Pop', 'king')

# INSERT INTO orders (customer_id, order_date, total_amount) VALUES 
# (1, '(2024-03-11)', 50)

# INSERT INTO orders (customer_id, order_date, total_amount) VALUES 
# (2, '(2024-03-10)', 112)

# UPDATE products
# SET price = 40
# WHERE id = 1;



