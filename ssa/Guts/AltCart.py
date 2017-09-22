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
        if self.user.status == "logged_in":
            # TODO: uncomment the address stuff when it is working
            # if not self.user.setUserAddress():
            #     return False
            if not self.user.setUserCCNUM():
                return False
            # prompt for confirmation
            os.system('cls' if os.name == 'nt' else 'clear')
            # self.user.printUserAddress()
            self.user.printUserCCNUM()
            # print("Your total is: " + str(itemTotal()) + "\n")
            confirm = input("Is the information displayed correct? Y/N\n")
            if confirm == 'Y' or confirm == 'y':
                finalConfirm = input("Would you like to confirm this purchase? Y/N\n")
                if finalConfirm == 'y' or finalConfirm == 'Y':
                    # put info and items in db
                    for each in self.cartItems:
                        each.changeItemQuantity()
                    return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                return False

        elif self.user.status == "not_logged_in":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please Log In To Purchase.")
            return False

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
