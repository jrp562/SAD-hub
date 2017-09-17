import os
from ssa.Guts.User import User
from ssa.Guts.Cart import Cart

def Menu(user, status):
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
            selection = Menu(user, user.status)

        elif selection == 2:
            for item in itemlist:
                #create menu for add to cart
                pass
            selection = Menu(user, status)

        elif selection == 3:
            #cart.showItems()
            selection = Menu(user, status)

        elif selection == 4:
            exit()

        else:
            print("Invalid selection, please try again.")
            selection = Menu(user, status)

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
