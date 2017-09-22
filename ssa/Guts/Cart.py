import os
from ssa.Guts.Item import Item


class Cart:
    def __init__(self, user):
        self.cartID = ''
        self.user = user
        self.cartItems = []

    def showItems(self, cartItems):
        print(*cartItems, sep='\n')

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
                        break
            elif self.user.status == "logged_in":
                # print address/credit card and ask if information displayed is correct
                print("Shipping Address: \n")
                self.user.printUserAddress()
                print("Credit Card Number: \n", self.user.cardNumber)
                # prompt for confirmation
                confirm = input("Is the information displayed correct? Y/N\n")
                if confirm == 'Y' or confirm == 'y':
                    finalConfirm = input("Would you like to confirm this purchase? Y/N\n")
                    if finalConfirm == 'y' or finalConfirm == 'Y':
                        # put info and items in db
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
        for each in self.cartItems:
            if each.itemID == itemID:
                del self.cartItems[each]
