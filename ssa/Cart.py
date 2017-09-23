import os
from Item import Item
import sqlite3


class Cart:
    def __init__(self, user):
        self.cartID = ''
        self.user = user
        self.cartItems = []

    def showItems(self):
        for each in self.cartItems:
            print((each.itemID, each.itemName, each.itemQuantity, each.itemCost), sep='\n')
            print("Total Cost: ", self.itemTotal())

    def purchaseCart(self):
        while 1:
            if self.user.status == "not_logged_in":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Please Log In To Purchase.")
                break
            elif self.user.status == "logged_in":
                # print address/credit card and ask if information displayed is correct
                creditCard = input("Please provide your credit card number: \n")
                print("Credit Card Number: \n", creditCard)
                print("Shipping Address: ")
                self.user.printUserAddress()
                # prompt for confirmation
                confirm = input("Is the information displayed correct? Y/N\n")
                if confirm == 'Y' or confirm == 'y':
                    finalConfirm = input("Would you like to confirm this purchase? Y/N\n")
                    if finalConfirm == 'y' or finalConfirm == 'Y':
                        # put info and items in db
                        sqliteFile = 'shop_db.db'
                        conn = sqlite3.connect(sqliteFile)
                        cursor = conn.cursor()
                        cursor.execute("SELECT DISTINCT cart_id FROM PURCHASE_HISTORY WHERE owner = ?", (self.user.userID,))
                        results = cursor.fetchall()
                        # Get next cartID
                        num = 0
                        for each in results:
                            num = each[0]
                        num += 1
                        # Enter into Purchase History
                        address = str(self.user.address)
                        for each in self.cartItems:
                            cursor.execute("INSERT INTO PURCHASE_HISTORY VALUES (?, ?, ?, ?, ?, ?, ?)", (num, each.itemID, each.itemCost, self.user.userID, creditCard, each.itemQuantity, address))
                            conn.commit()
                        # commit changes to DB

                        conn.close()
                        for each in self.cartItems:
                            each.changeItemQuantity()
                        break

    def itemTotal(self):
        total = 0.0
        for each in self.cartItems:
            total += each.itemCost * each.itemQuantity

        print("$", total)

    def addItem(self, itemID, quantity):
        newItem = Item(itemID, quantity)
        self.cartItems.append(newItem)

    def removeItem(self, itemID):
        for i in range(len(self.cartItems)):
            if self.cartItems[i].itemID == itemID:
                del self.cartItems[i]
