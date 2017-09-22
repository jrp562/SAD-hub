import os
from ssa.Guts.User import User
from ssa.Guts.AltCart import Cart

def Menu(user, status, cart):
    if (status == 'not_logged_in'):
        selection = '0'
        print()
        print("*********Super Store App***********")
        print("1. Login")
        print("2. View Products")
        print("3. View Cart")
        print("4. Exit")
        selection = input("Please make a selection: ")


        if selection == '1':
            uname = input("Username: ")
            pword = input("Password: ")
            user.logIn(uname, pword)
            os.system('cls' if os.name == 'nt' else 'clear')
            selection = Menu(user, user.status, cart)

        elif selection == '2':
            #access db to get itemList or use cart class function to return the itemlist
            os.system('cls' if os.name == 'nt' else 'clear')
            print ('*********** Our Products ************')
            itemList = ['Boots', 'Grapefruit', 'Headphones', 'How to Use a Hammer by Pinky', 'Atlas', 'Shingles', 'Football', 'Great Expectations']
            i = 1
            for item in itemList:
                print (str(i) + '. ' + item)
                i = i + 1
            print ('')
            print ('************* Options *****************')
            print("1. Add an item to cart.")
            print("2. View Details.")
            print("3. Go Back.")
            selection = input("Please make a selection: ")

            if selection == '1':
                # do crazy shit
                pass

            elif selection == '2':
                #cart.purchaseCart()
                pass

            elif selection == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                selection = Menu(user, user.status, cart)

            else:
                erroneousInput(user, cart)


        elif selection == '3':
            #get data from cart and add to list
            os.system('cls' if os.name == 'nt' else 'clear')
            print ('*********** Your Cart ************')
            itemList = ['Boots', 'Grapefruit', 'Headphones', 'How to Use a Hammer by Pinky']
            i = 1
            for item in itemList:
                print (str(i) + '. ' + item)
                i = i + 1
            print ('')
            print ('************* Cart Options *****************')
            print("1. Remove an item from cart.")
            print("2. Purchase cart.")
            print("3. Go Back.")
            selection = input("Please make a selection: ")

            if selection == '1':
                # do crazy shit
                pass

            elif selection == '2':
                #purchaseCart()
                pass

            elif selection == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                selection = Menu(user, user.status, cart)

            else:
                erroneousInput(user, cart)

        elif selection == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()

        else:
            erroneousInput(user, cart)

        return selection

    if (status == 'logged_in'):
        selection = '0'
        print()
        print("*********Super Store App***********")
        print("1. View Purchase History")
        print("2. View Products")
        print("3. View Cart")
        print("4. Log Off / Exit")
        selection = input("Please make a selection: ")

        if selection == '1':
            user.getPurchaseHistory()
            selection = Menu(user, user.status, cart)

        elif selection == '2':
            #access db to get itemList
            os.system('cls' if os.name == 'nt' else 'clear')
            print ('*********** Our Products ************')
            itemList = ['Boots', 'Grapefruit', 'Headphones', 'How to Use a Hammer by Pinky', 'Atlas', 'Shingles', 'Football', 'Great Expectations']
            i = 1
            for item in itemList:
                print (str(i) + '. ' + item)
                i = i + 1
            print ('')
            print ('*************** Options *****************')
            print("1. Add an item to cart.")
            print("2. Go Back.")
            selection = input("Please make a selection: ")

            if selection == '1':
                # do crazy shit
                pass

            elif selection == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                selection = Menu(user, user.status, cart)

            else:
                erroneousInput(user, cart)

        elif selection == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print ('***********' + user.username + ' Cart ************')
            itemList = ['Boots', 'Grapefruit', 'Headphones', 'How to Use a Hammer by Pinky']
            i = 1
            for item in itemList:
                print (str(i) + '. ' + item)
                i = i + 1
            print ('')
            print ('************* Cart Options *****************')
            print("1. Remove an item from cart.")
            print("2. Purchase cart.")
            print("3. Go Back.")
            selection = input("Please make a selection: ")

            if selection == '1':
                # do crazy shit
                pass

            elif selection == '2':
                #purchaseCart()
                pass

            elif selection == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                selection = Menu(user, user.status, cart)

            else:
                erroneousInput(user, cart)

        elif selection == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()

        else:
            erroneousInput(user, cart)


def itemMenu(itemList):
    pass


def erroneousInput(user, cart):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Invalid selection, please try again.")
    selection = Menu(user, user.status, cart)
