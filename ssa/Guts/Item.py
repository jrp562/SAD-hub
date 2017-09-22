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

    def GetItem(self):
        self.cursor.execute('select item_id, item_cost, item_quan, item_name, item_desc from inventory')
        row = self.cursor.fetchone()
        for row in data:
            self.itemId = row[0]
            self.itemCost = row[1]
            self.itemQuantity = row[2]
            self.itemName = row[3]
            self.itemDescription = row[4]

    def GetItemName(self):
        return self.itemName

    def GetItemCost(self):
        return self.itemCost

    def ChangeItemQuantity(self, newQuantity):
        self.cursor.execute('update inventory set item_quan=%s where item_id = %s', (newQuantity, self.itemName))

    def ChangeItemCost(self, newCost):
        self.ItemCost = newCost
