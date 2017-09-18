import os

class Cart:
    def __init__(self, user):
        self.cartid = ''
        self.user = user

    def showItems(self):
        #get cart items from db and insert into list
        itemList = ['monkeys', 'book', 'thong', 'riding crop']
        os.system('cls' if os.name == 'nt' else 'clear')
        print ('***********' + self.user.username + ' Cart ************')
        itemList = ['dildo', 'Grapefruit', 'KY', 'How to Use a Dildo by Pinky']
        i = 1
        for item in itemList:
            print (str(i) + '. ' + item)
            i = i + 1
        print ('')
        print ('************* Cart Options *****************')
        print("1. Remove an item from cart.")
        print("2. Purchase cart.")
        selection = int(input("Please make a selection: "))

        if selection == 1:
            # do crazy shit
            pass

        elif selection == 2:
            #purchaseCart()
            pass

    def purchaseCart(self):
        #prompt for address/creditcard
        #prompt for confirmation
        #put info and items into db
        pass
