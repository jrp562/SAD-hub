import os
from ssa.Item import Item


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
                # prompt for address/credit card if not logged in
                address = input("Please enter your address for shipping purposes: \n")
                creditCard = input("Please provide your credit card number: \n")
                print("Shipping Address: \n", address, "\nCredit Card Number: \n", creditCard)
                # prompt for confirmation
                confirm = input("Is the information displayed correct? Y/N\n")
                if confirm == 'Y' or confirm == 'y':
                    finalConfirm = input("Would you like to confirm this purchase? Y/N\n")
                    if finalConfirm == 'y' or finalConfirm == 'Y':
                        # put info and items in db
                        for each in self.cartItems:
                            each.changeItemQuantity()
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
