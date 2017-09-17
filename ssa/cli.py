def main():
    import os
    from ssa.Guts.User import User
    from ssa.Guts.Cart import Cart
    from ssa.Guts.Menu import Menu

    os.system('cls' if os.name == 'nt' else 'clear')
    user = User()
    cart = Cart()
    Menu(user, user.status)
