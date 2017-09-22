import sqlite3

sqlite_file = 'shop_db.sqlite'
#create table names
inventory = 'inventory'
shopping_cart = 'shopping_cart'
users = 'users'
#specify fields needed for each table

#connect to the database
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#create new SQLite table
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
	.format(tn=inventory, nf=new_field, ft=field_type))

#commit and close changes to db
conn.commit()
conn.close()