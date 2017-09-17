from ssa.Guts.Cart import Cart

class User:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.status = 'not_logged_in'

    def logIn(self, username, password):
        self.username = username
        self.password = password
        #check against db here
        self.status = 'logged_in'
        return self.status
