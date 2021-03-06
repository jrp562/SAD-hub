import sqlite3


class Item:
    def __init__(self, itemID, quantity):
        self.itemID = itemID
        self.itemCost = 0.00
        self.itemQuantity = quantity
        self.itemName = ''
        self.itemDescription = ''
        self.itemCategory = ''
        self.getItem()

    def getItem(self):
        sqliteFile = 'shop_db.db'
        conn = sqlite3.connect(sqliteFile)
        cursor = conn.cursor()
        cursor.execute("SELECT price, quantity, name, description FROM INVENTORY WHERE ID = '%s' " % self.itemID)
        # Get the item info from the database.
        row = cursor.fetchone()
        self.itemCost = row[0]
        self.itemName = row[2]
        self.itemDescription = row[3]
        conn.close()

    def changeItemQuantity(self):
        sqliteFile = 'shop_db.db'
        conn = sqlite3.connect(sqliteFile)
        cursor = conn.cursor()
        # Get current quantity
        cursor.execute("Select quantity FROM INVENTORY WHERE ID = '%s'" % self.itemID)
        result = cursor.fetchone()
        newQuantity = result[0] - self.itemQuantity
        # update quantity in DB, commit, and close connection
        cursor.execute("update inventory set quantity = ? where ID = ?", (newQuantity, self.itemID,))
        conn.commit()
        conn.close()


class Toys (Item):
    def __init__(self, itemID, quantity):
        super().__init__(itemID, quantity)
        self.isActionFigure = False
        self.ageRange = ''
        self.itemCategory = 'Toy'

        # Connect and get pertinent info from db
        sqliteFile = 'shop_db.db'
        conn = sqlite3.connect(sqliteFile)
        cursor = conn.cursor()
        cursor.execute("SELECT age, isActionFigure FROM TOYS_INVENTORY WHERE ID = '%s' " % self.itemID)
        result = cursor.fetchone()

        self.ageRange = result[0]
        self.isActionFigure = result[1]

        conn.close()


class Book (Item):
    def __init__(self, itemID, quantity):
        super().__init__(itemID, quantity)
        self.isbn = 0
        self.author = ''
        self.itemCategory = 'Book'

        # Connect and get pertinent info from db
        sqliteFile = 'shop_db.db'
        conn = sqlite3.connect(sqliteFile)
        cursor = conn.cursor()
        cursor.execute("SELECT ISBN, author FROM BOOKS_TABLE WHERE ID = '%s' " % self.itemID)
        result = cursor.fetchone()

        self.isbn = result[0]
        self.author = result[1]
        conn.close()


class Household (Item):
    def __init__(self, itemID, quantity):
        super().__init__(itemID, quantity)
        self.room = ''
        self.isLuxuryItem = False
        self.itemCategory = 'Household item'

        # Connect and get pertinent info from db
        sqliteFile = 'shop_db.db'
        conn = sqlite3.connect(sqliteFile)
        cursor = conn.cursor()
        cursor.execute("SELECT room, isluxuryitem FROM HH_INVENTORY WHERE ID = '%s' " % self.itemID)
        result = cursor.fetchone()

        self.room = result[0]
        self.isLuxuryItem = result[1]
        conn.close()


class Electronic (Item):
    def __init__(self, itemID, quantity):
        super().__init__(itemID, quantity)
        self.brand = ''
        self.category = ''
        self.itemCategory = 'electronic'

        # Connect and get pertinent info from db
        sqliteFile = 'shop_db.db'
        conn = sqlite3.connect(sqliteFile)
        cursor = conn.cursor()
        cursor.execute("SELECT brand, category FROM ELEC_INVENTORY WHERE ID = '%s' " % self.itemID)
        result = cursor.fetchone()

        self.brand = result[0]
        self.category = result[1]
        conn.close()


class Clothes (Item):
    def __init__(self, itemID, quantity):
        super().__init__(itemID, quantity)
        self.gender = ''
        self.section = ''
        self.itemCategory = 'clothing'

        # Connect and get pertinent info from db
        sqliteFile = 'shop_db.db'
        conn = sqlite3.connect(sqliteFile)
        cursor = conn.cursor()
        cursor.execute("SELECT gender, section FROM ELEC_INVENTORY WHERE ID = '%s' " % self.itemID)
        result = cursor.fetchone()

        self.gender = result[0]
        self.section = result[1]
        conn.close()
