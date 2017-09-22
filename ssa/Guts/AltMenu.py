import os
from ssa.Guts.User import User
from ssa.Guts.Cart import Cart


def mainMenu(user, cart):
    if (user.status == 'not_logged_in'):
        selection = '0'
        print()
        print("*********Super Store App***********")
        print("1. Login")
        print("2. View Products")
        print("3. View Cart")
        print("4. Exit")
        selection = input("Please make a selection: ")
        if selection == '1':
            menuChoice(user, cart, '1')
        elif selection == '2':
            menuChoice(user, cart, '2')
        elif selection == '3':
            menuChoice(user, cart, '3')
        elif selection == '4':
            menuChoice(user, cart, '9')
        else:
            menuChoice(user, cart, 'not_valid')

    elif (user.status == 'logged_in'):
        selection = '0'
        print()
        print("*********Super Store App***********")
        print("1. View Purchase History")
        print("2. View Products")
        print("3. View Cart")
        print("4. Log Off / Exit")
        selection = input("Please make a selection: ")
        if selection == '1':
            menuChoice(user, cart, '4')
        elif selection == '2':
            menuChoice(user, cart, '2')
        elif selection == '3':
            menuChoice(user, cart, '3')
        elif selection == '4':
            menuChoice(user, cart, '9')
        else:
            menuChoice(user, cart, 'not_valid')


def menuChoice(user, cart, selection):
    os.system('cls' if os.name == 'nt' else 'clear')
    if selection == '':
        menus['0'](user, cart)
    else:
        try:
            menus[selection](user, cart)
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menus['0'](user, cart)
    return

def menuLogin(user, cart):
    print ('*********** Login ************')
    uname = input("Username: ")
    pword = input("Password: ")
    user.logIn(uname, pword)
    os.system('cls' if os.name == 'nt' else 'clear')
    menuChoice(user, cart, '0')

def menuProducts(user, cart):
    os.system('cls' if os.name == 'nt' else 'clear')
    print ('*********** Our Products ************')
    itemList = ['Boots', 'Grapefruit', 'Headphones', 'How to Use a Hammer by Pinky', 'Atlas', 'Shingles', 'Football', 'Great Expectations']
    printMenuList(itemList)
    print ('')
    print ('************* Options *****************')
    print("1. Add an item to cart.")
    print("2. Go Back.")
    selection = input("Please make a selection: ")
    if selection == '1':
        menuChoice(user, cart, '6')
    elif selection == '3':
        menuChoice(user, cart, '0')
    else:
        menuChoice(user, cart, 'not_valid')

def menuCart(user, cart):
    print ('*********** Your Cart ************')
    itemList = ['Boots', 'Grapefruit', 'Headphones', 'How to Use a Hammer by Pinky']
    printMenuList(itemList)
    print ('')
    print ('************* Cart Options *****************')
    print("1. Remove an item from cart.")
    print("2. Purchase cart.")
    print("3. Go Back.")
    selection = input("Please make a selection: ")
    if selection == '1':
        menuChoice(user, cart, '7')
    elif selection == '2':
        menuChoice(user, cart, '5')
    elif selection == '3':
        menuChoice(user, cart, '0')
    else:
        menuChoice(user, cart, 'not_valid')

def menuPurchase(user, cart):
    pass

def menuPurchaseHistory(user, cart):
    print('***********Your Purchase History ************')
    user.getPurchaseHistory()
    mainMenu(user, cart)

def menuAddToCart(user, cart):
    pass

def menuRemoveFromCart(user, cart):
    pass

def menuExit(user, cart):
    exit()

def printMenuList(itemList):
    i = 0
    for item in itemList:
        print (str(i) + '. ' + item)
        i = i + 1

menus = {
    '0' : mainMenu,
    '1' : menuLogin,
    '2' : menuProducts,
    '3' : menuCart,
    '4' : menuPurchaseHistory,
    '5' : menuPurchase,
    '6' : menuAddToCart,
    '7' : menuRemoveFromCart,
    '9' : menuExit}
