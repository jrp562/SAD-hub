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

    # TODO: this needs to be worked on
    def getPurchaseHistory(self):
        sqliteFile = 'shop_db.db'
        conn = sqlite3.connect(sqliteFile)
        cursor = conn.cursor()
        cursor.execute("SELECT ITEM_NAME, DATES FROM PURCHASE_HISTORY WHERE USER_ID = ?", (self.userID,))
        row = cursor.fetchall()
        # print (row)
        for item in row:
            print(item[0] + '\t\t\t' + item[1])
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
