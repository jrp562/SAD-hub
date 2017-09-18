import os
from ssa.Guts.User import User
from ssa.Guts.Cart import Cart

def Menu(user, status, cart):
    if (status == 'not_logged_in'):
        selection = 0
        print()
        print("*********Super Store App***********")
        print("1. Login")
        print("2. View Products")
        print("3. View Cart")
        print("4. Exit")
        selection = int(input("Please make a selection: "))

        if selection == 1:
            uname = input("Username: ")
            pword = input("Password: ")
            user.logIn(uname, pword)
            os.system('cls' if os.name == 'nt' else 'clear')
            selection = Menu(user, user.status, cart)

        elif selection == 2:
            #access db to get itemList
            os.system('cls' if os.name == 'nt' else 'clear')
            print ('*********** Our Products ************')
            itemList = ['dildo', 'Grapefruit', 'KY', 'How to Use a Dildo by Pinky', 'crap', 'shit', 'something else', 'a book about something']
            i = 1
            for item in itemList:
                print (str(i) + '. ' + item)
                i = i + 1
            print ('')
            print ('************* Cart Options *****************')
            print("1. Add an item to cart.")
            print("2. View Desription.")
            selection = int(input("Please make a selection: "))

            if selection == 1:
                # do crazy shit
                pass

            elif selection == 2:
                #purchaseCart()
                pass

        elif selection == 3:
            cart.showItems()
            selection = Menu(user, status, cart)

        elif selection == 4:
            exit()

        else:
            print("Invalid selection, please try again.")
            selection = Menu(user, status, cart)

        return selection

    if (status == 'logged_in'):
        selection = 0
        print()
        print("*********Super Store App***********")
        print("1. View Purchase History")
        print("2. View Products")
        print("3. View Cart")
        print("4. Log Off / Exit")
        selection = int(input("Please make a selection: "))

        if selection == 1:
            user.getPurchaseHistory()
            selection = Menu(user, status, cart)

        elif selection == 2:
            #access db to get itemList
            os.system('cls' if os.name == 'nt' else 'clear')
            print ('*********** Our Products ************')
            itemList = ['dildo', 'Grapefruit', 'KY', 'How to Use a Dildo by Pinky', 'crap', 'shit', 'something else', 'a book about something']
            i = 1
            for item in itemList:
                print (str(i) + '. ' + item)
                i = i + 1
            print ('')
            print ('************* Cart Options *****************')
            print("1. Add an item to cart.")
            print("2. View Desription.")
            selection = int(input("Please make a selection: "))

            if selection == 1:
                # do crazy shit
                pass

            elif selection == 2:
                #purchaseCart()
                pass

        elif selection == 3:
            cart.showItems()
            pass

        elif selection == 4:
            exit()

        else:
            print("Invalid selection, please try again.")
            os.system('cls' if os.name == 'nt' else 'clear')
            selection = Menu(user, status, cart)


def itemMenu(itemList):
    pass
