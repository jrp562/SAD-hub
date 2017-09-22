import os
import sqlite3
from ssa.Guts.Cart import Cart

class User:
    def __init__(self):
        self.userID = 0
        self.username = ''
        self.address = []
        self.cardNumber = 0
        self.status = 'not_logged_in'

    def logIn(self, username, password):
        self.username = username
    # check against db here and get userID
        sqlite_file = 'shop_db.db'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute("SELECT * FROM Users WHERE USER_NAME=?", (self.username, ))
        data = c.fetchall()
        # print (data)
    # check password and set variables if correct
        if (data[0][2] == password):
            self.status = 'logged_in'
            self.userID = data[0][0]
            self.username = data[0][1]
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
        # access db for a list of items adn dates then put into itemList
        os.system('cls' if os.name == 'nt' else 'clear')
        print('***********' + self.username + ' Purchase History ************')
        itemList = ['Hammer', 'Grapefruit',
                    'Boots', 'How to Use a Hammer by Pinky']
        i = 1
        for item in itemList:
            print(str(i) + '. ' + item + '    Date: 12/23/2016')
            i = i + 1

    def getUserAddress(self):
        if (self.status == 'not_logged_in' and self.userID != 0):
            loadUserData(self.userID)
            return self.address
        elif (self.status == 'not_logged_in' and self.userID == 0):
            # big error?
            pass
        else:
            return self.address

    def printUserAddress(self):
        print (self.address[0])
        print (self.address[1] + ", " + self.address[2] + " " + self.address[3])

    def getUsername(self):
        if (self.status == 'not_logged_in' and self.userID != 0):
            loadUserData(self.userID)
            return self.username
        elif (self.status == 'not_logged_in' and self.userID == 0):
            # big error?
            pass
        else:
            return self.username

    def getCCNUM(self):
        if (self.status == 'not_logged_in' and self.userID != 0):
            loadUserData(self.userID)
            return self.creditCardNumber
        elif (self.status == 'not_logged_in' and self.userID == 0):
            # big error?
            pass
        else:
            return self.creditCardNumber

    def loadUserData(self, userID):
        # take list from db and update values
        pass

    def setUserAddress(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('*********** Please enter Address ************')
        address[0] = input("Enter the number and street of your address: ")
        address[1] = input("Enter the city: ")
        address[2] = input("Enter the state: ")
        address[3] = int(input("Enter your zipcode: "))
        # create insert statement for db

    def setUserCCNUM(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('*********** Please enter your card Number ************')
        self.cardNumber = int(input("Card Number:"))
        if (len(str(self.cardNumber)) != 10):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(' Invalid Card Number! ')
            return False
        else:
            print("Would like us to save your Card Number? (y/n): ")
            answer = input()
            if (answer == 'y'):
                # insert into db
                pass
            elif (answer == 'n'):
                print("Card number not saved.")
                return True
            else:
                print("User input not recognized. Card number not saved.")
                return True
