import sqlite3

connection = sqlite3.connect("transactions.db")
cursor = connection.cursor()

createTableCommand = """ CREATE TABLE IF NOT EXISTS stores(store_id
INTEGER PRIMARY KEY, location TEXT) """

cursor.execute(createTableCommand)

createTableCommand2 = """ CREATE TABLE IF NOT EXISTS purchases(purchase_id
INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT, FOREIGN KEY(store_id)
REFERENCES stores(store_id)) """

cursor.execute(createTableCommand2)

cursor.execute("INSERT INTO stores VALUES (21, 'A city, NY')")
cursor.execute("INSERT INTO stores VALUES (31, 'A city, NY')")
cursor.execute("INSERT INTO stores VALUES (41, 'A city, NY')")

cursor.execute("INSERT INTO purchases VALUES (54, 21, 15.69)")
cursor.execute("INSERT INTO purchases VALUES (20, 11, 20.69)")

cursor.execute("SELECT * FROM stores")
results = cursor.fetchall()

print(results)
