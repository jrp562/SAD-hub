import os
import sqlite3
from ssa.Guts.AltCart import Cart

class User:
    def __init__(self):
        self.userID = 0
        self.username = ''
        self.address = ['', '', '', '']
        self.cardData = ['', '', '', '', '']
        self.status = 'not_logged_in'

    def logIn(self, username, password):
        self.username = username
    # check against db here and get userID
        sqlite_file = 'shop_db.db'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute("SELECT * FROM Users WHERE USER_NAME=?", (self.username, ))
        data = c.fetchall()
        print (data)
    # check password and set variables if correct
    # TODO: needs to be updated when db is updated
        if (data[0][2] == password):
            self.status = 'logged_in'
            self.userID = data[0][0]
            self.username = data[0][1]
            self.address[0] = data[0][2]
            self.address[1] = data[0][3]
            self.address[2] = data[0][4]
            self.address[3] = data[0][5]
        conn.close()
        return self.status

    def logout(self):
        self.userID = 0
        self.username = ''
        self.password = ''
        self.address = []
        self.creditCardNumber = 0
        self.status = 'not_logged_in'

    def getPurchaseHistory(self):
        sqlite_file = 'shop_db.db'
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()
        cursor.execute("SELECT ITEM_NAME, DATES FROM PURCHASE_HISTORY WHERE USER_ID = ?", (self.userID, ))
        row = cursor.fetchall()
        # print (row)
        for item in row:
            print (item[0] + '\t\t\t' + item[1])
        return

    def getUserAddress(self):
        return self.address

    def printUserAddress(self):
        print (str(self.address[0]))
        print (str(self.address[1]) + ", " + str(self.address[2]) + " " + str(self.address[3]))

    def getUsername(self):
        return self.username

    def getCCNUM(self):
        return self.cardData[1]

    def setUserAddress(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('*********** Please Enter Your Address ************')
        self.address[0] = input("Enter the number and street of your address: ")
        self.address[1] = input("Enter the city: ")
        self.address[2] = input("Enter the state: ")
        self.address[3] = input("Enter your zipcode: ")
        sqlite_file = 'shop_db.db'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        # TODO: fix this shit
        c.execute("INSERT INTO USERS (ADDRLINE1, CITY, STATE, ZIP) VALUES (?,?,?,?) WHERE USER_ID=?", (self.address[0], self.address[1], self.address[2], self.address[3], self.userID))
        conn.commit()
        conn.close()
        return True

    def setUserCCNUM(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('*********** Please enter your card Number ************')
        self.cardData[0] = input("Name on Card: ")
        self.cardData[1] = int(input("Card Number:"))
        self.cardData[2] = input("ccv: ")
        self.cardData[3] = input("Expiration Month: ")
        self.cardData[4] = input("Expiration Year: ")
        if (len(str(self.cardData[1])) != 10):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(' Invalid Card Number! ')
            return False
        else:
            return True

    def printUserCCNUM(self):
        print("*********** Card Info ************")
        for item in self.cardData:
            print(str(item))
        pass
