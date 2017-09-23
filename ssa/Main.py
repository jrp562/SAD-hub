import os
from User import User
from Cart import Cart
from Menu import mainMenu, menuLogin, menuCart, menuProducts, menuPurchaseHistory, menuPurchase, \
    menuExit, menuAddToCart, menuRemoveFromCart


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    user = User()
    cart = Cart(user)
    mainMenu(user, cart)
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

    menus['0'](user, cart)


main()
