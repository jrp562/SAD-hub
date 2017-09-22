def main():
    import os
    from ssa.Guts.User import User
    from ssa.Guts.AltCart import Cart
    # from ssa.Guts.Menu import Menu
    from ssa.Guts.AltMenu import mainMenu, menuChoice, menuLogin, menuCart, menuProducts, menuPurchaseHistory, menuPurchase, menuExit, printMenuList, menuAddToCart, menuRemoveFromCart

    os.system('cls' if os.name == 'nt' else 'clear')
    user = User()
    cart = Cart(user)
    # Menu(user, user.status, cart)
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

    menus['0'](user, cart)
