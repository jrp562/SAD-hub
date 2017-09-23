import os
import sqlite3


class User:
    def __init__(self):
        self.userID = 0
        self.username = ''
        self.password = ''
        self.address = ''
        self.status = 'not_logged_in'

    def logIn(self, username, password):
        self.username = username
        self.password = password
        # check against db here and get userID
        sqliteFile = 'shop_db.db'
        conn = sqlite3.connect(sqliteFile)
        c = conn.cursor()
        c.execute("SELECT * FROM Users WHERE USER_NAME=? AND PASSWORD=?", (self.username, self.password,))
        data = c.fetchone()
        if data is None:
            print("No such username/password combination found. Please try again.\n")
            conn.close()
            return self.status
        else:
            self.status = 'logged_in'
            self.userID = data[0]
            self.username = data[1]
            c.execute("SELECT ADDRESS FROM USERS")
            address = c.fetchone()
            self.address = address
            conn.close()
            return self.status

    def logout(self):
        self.userID = 0
        self.username = ''
        self.password = ''
        self.address = []
        self.status = 'not_logged_in'

    def getPurchaseHistory(self):
        sqliteFile = 'shop_db.db'
        conn = sqlite3.connect(sqliteFile)
        cursor = conn.cursor()
        cursor.execute("SELECT inv.name, cart.item_quantity, cart.price, cart.cart_id, cart.ccard, "
                       "cart.address FROM INVENTORY as inv, "
                       "PURCHASE_HISTORY as cart WHERE inv.ID = cart.item AND cart.owner = ?", (self.userID,))
        results = cursor.fetchall()
        cartID = 1
        total = 0
        card = 0
        address = ''
        for each in results:
            if each[3] != cartID:
                print("Credit card: ", card)
                print("Shipping Address: ", address)
                print("Total Cart Price: ", total)
                total = 0
                cartID = each[3]
            print("Item: ", each[0], "\tQuantity: ", each[1], "\tPrice: ", each[2])
            total += each[1] * each[2]
            card = each[4]
            address = each[5]
        # Print the last cart's card, address, and total.
        print("Credit card: ", card)
        print("Shipping Address: ", address)
        print("Total Cart Price: ", total)
        # Close the connection
        conn.close()
        return

    def getUserAddress(self):
        return self.address

    def printUserAddress(self):
        print(self.address)

    def getUsername(self):
        return self.username

    def setUserAddress(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('******************************************')
        self.address = input("Please Enter Your Address: ")
        sqlite_file = 'shop_db.db'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute("INSERT INTO USERS ADDRESS VALUE (?) WHERE USER_ID= ?", (self.address, self.userID))
        conn.commit()
        conn.close()
        return True

    '''def getCCNUM(self):
        return self.cardData[1]

    def setUserCCNUM(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('*********** Please enter your card Number ************')
        self.cardData[0] = input("Name on Card: ")
        self.cardData[1] = int(input("Card Number:"))
        self.cardData[2] = input("ccv: ")
        self.cardData[3] = input("Expiration Month: ")
        self.cardData[4] = input("Expiration Year: ")
        if len(str(self.cardData[1])) != 10:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(' Invalid Card Number! ')
            return False
        else:
            return True

    def printUserCCNUM(self):
        print("*********** Card Info ************")
        for item in self.cardData:
            print(str(item))
        pass'''
