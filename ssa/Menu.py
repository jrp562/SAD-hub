import os
import sqlite3


def mainMenu(user, cart):
    if user.status == 'not_logged_in':
        print("*********Super Store App***********")
        print(" 1. Login\n", "2. View Products\n", "3. View Cart\n", "4. Exit\n")
        selection = input("Please make a selection: ")
        if selection == '1':
            menuChoice(user, cart, '1')
        elif selection == '2':
            menuChoice(user, cart, '2')
        elif selection == '3':
            menuChoice(user, cart, '3')
        elif selection == '4':
            menuChoice(user, cart, '9')

    elif user.status == 'logged_in':
        print("*********Super Store App***********")
        print("1. View Purchase History\n", "2. View Products\n", "3. View Cart\n", "4. Log Off / Exit\n")
        selection = input("Please make a selection: ")
        if selection == '1':
            menuChoice(user, cart, '4')
        elif selection == '2':
            menuChoice(user, cart, '2')
        elif selection == '3':
            menuChoice(user, cart, '3')
        elif selection == '4':
            menuChoice(user, cart, '9')


def menuChoice(user, cart, selection):
    os.system('cls' if os.name == 'nt' else 'clear')
    if selection == '':
        menus['0']()
    else:
        try:
            menus[selection](user, cart)
        except KeyError:
            print("Invalid selection, please try again.\n")
            menus['0'](user, cart)
    return


def menuLogin(user, cart):
    print('*********** Login ************')
    username = input("Username: ")
    password = input("Password: ")
    user.logIn(username, password)
    os.system('cls' if os.name == 'nt' else 'clear')
    menuChoice(user, cart, '0')


def menuProducts(user, cart):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*********** Our Products ************')
    sqliteFile = 'shop_db.db'
    conn = sqlite3.connect(sqliteFile)
    c = conn.cursor()
    for row in c.execute("SELECT * FROM inventory"):
        print(row)
    print('\n************* Options *****************')
    print("1. Add an item to cart.\n", "2. Go Back.\n")
    selection = input("Please make a selection: ")
    if selection == '1':
        menuChoice(user, cart, '6')
    elif selection == '2':
        menuChoice(user, cart, '0')


def menuCart(user, cart):
    print('*********** Your Cart ************')
    cart.showItems()
    print('\n************* Cart Options *****************')
    print("1. Remove an item from cart.\n", "2. Purchase cart.\n", "3. Go Back.\n")
    selection = input("Please make a selection: ")
    if selection == '1':
        menuChoice(user, cart, '7')
    elif selection == '2':
        menuChoice(user, cart, '5')
    elif selection == '3':
        menuChoice(user, cart, '0')


def menuPurchase(user, cart):
    cart.purchaseCart()
    mainMenu(user, cart)


def menuPurchaseHistory(user, cart):
    user.getPurchaseHistory()
    mainMenu(user, cart)


def menuAddToCart(user, cart):
    print('*********** Categories ************')
    print(' 1. Books\n', '2. Electronics\n', '3. Clothes\n', '4. Household Items\n', '5. Toys\n')
    selection = int(input("Please select which category of products to view: "))
    if selection == 1:
        selection = 'BOOKS_TABLE'
    elif selection == 2:
        selection = 'ELEC_INVENTORY'
    elif selection == 3:
        selection = 'CLOTHES_INVENTORY'
    elif selection == 4:
        selection = 'HH_INVENTORY'
    elif selection == 5:
        selection = 'TOYS_INVENTORY'
    else:
        erroneousInput(user, cart)
    conn = sqlite3.connect('shop_db.db')
    c = conn.cursor()
    for row in c.execute("SELECT s.*, i.price, i.quantity FROM '%s' as s, INVENTORY as i WHERE s.ID = i.ID" % selection):
        print(row)
    itemID = int(input("Please provide the ID number of the item you would like to add to the cart: "))
    quantity = int(input("Please provide the quantity of the item you would like to add: "))
    cart.addItem(itemID, quantity)
    mainMenu(user, cart)


def menuRemoveFromCart(user, cart):
    cart.showItems()
    itemID = int(input("Please provide the ID number of the item you would like to remove: "))
    cart.removeItem(itemID)
    mainMenu(user, cart)


def menuExit():
    exit()


def erroneousInput(user, cart):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Invalid selection, please try again.")
    menuChoice(user, cart, '0')


def printMenuList(itemList):
    i = 0
    for item in itemList:
        print(str(i) + '. ' + item)
        i = i + 1


menus = {
    '0': mainMenu,
    '1': menuLogin,
    '2': menuProducts,
    '3': menuCart,
    '4': menuPurchaseHistory,
    '5': menuPurchase,
    '6': menuAddToCart,
    '7': menuRemoveFromCart,
    '9': menuExit}
