import sqlite3

from ssa.Guts.db import conn, sqlite_file


class Item:
    def __init__(self):
        self.itemId = ''
        self.itemCost = 0.00
        self.itemQuantity = 0
        self.itemName = ''
        self.itemDescription = ''
        self.category = ''
        self.conn = sqlite3.connect(sqlite_file)
        self.cursor = conn.cursor()

    def getItem(self):
        data = self.cursor.execute('select item_id, item_cost, item_quan, item_name, item_desc from inventory')
        row = self.cursor.fetchone()
        for row in data:
            self.itemId = row[0]
            self.itemCost = row[1]
            self.itemQuantity = row[2]
            self.itemName = row[3]
            self.itemDescription = row[4]

    def getItemName(self):
        return self.itemName

    def getItemCost(self):
        return self.itemCost

    def changeItemQuantity(self, newQuantity):
        self.cursor.execute('update inventory set item_quan=%s where item_id = %s', (newQuantity, self.itemName))

    def changeItemCost(self, newCost):
        self.itemCost = newCost


class Toys (Item):
    def __init__(self):
        super().__init__()
        self.isActionFigure = False
        self.ageRange = ''


class Book (Item):
    def __init__(self):
        super().__init__()
        self.isbn = ''
        self.author = ''


class Household (Item):
    def __init__(self):
        super().__init__()
        self.room = ''
        self.isLuxuryItem = False


class Electronic (Item):
    def __init__(self):
        super().__init__()
        self.brand = ''
        self.category = ''
