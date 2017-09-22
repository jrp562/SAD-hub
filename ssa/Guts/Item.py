import sqlite3

from ssa.Guts.db import conn, sqlite_file


class Item:
    def __init__(self, itemid, quantity):
        self.itemID = itemid
        self.itemCost = 0.00
        self.itemQuantity = quantity
        self.itemName = ''
        self.itemDescription = ''
        self.category = ''
        self.conn = sqlite3.connect(sqlite_file)
        self.cursor = conn.cursor()

    def getItem(self):
        self.cursor.execute('SELECT price, quantity, name, description FROM INVENTORY WHERE ID = ', self.itemId, ';')
        # Get the
        row = self.cursor.fetchone()
        self.itemCost = row[0]
        self.itemQuantity = row[1]
        self.itemName = row[2]
        self.itemDescription = row[3]

    def getItemName(self):
        return self.itemName

    def getItemCost(self):
        return self.itemCost

    def changeItemQuantity(self, newQuantity):
        self.cursor.execute('update inventory set item_quan=%s where item_id = %s', (newQuantity, self.itemName))


class Toys (Item):
    def __init__(self, itemID, quantity):
        super().__init__(itemID, quantity)
        self.isActionFigure = False
        self.ageRange = ''
        self.category = 'toy'


class Book (Item):
    def __init__(self, itemID, quantity):
        super().__init__(itemID, quantity)
        self.isbn = ''
        self.author = ''
        self.category = 'book'


class Household (Item):
    def __init__(self, itemID, quantity):
        super().__init__(itemID, quantity)
        self.room = ''
        self.isLuxuryItem = False
        self.category = 'household item'


class Electronic (Item):
    def __init__(self,itemID, quantity):
        super().__init__(itemID, quantity)
        self.brand = ''
        self.category = ''
        self.category = 'electronic'
