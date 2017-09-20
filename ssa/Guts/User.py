import os
from ssa.Guts.Cart import Cart

class User:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.address = ''
        self.status = 'not_logged_in'


    def logIn(self, username, password):
        self.username = username
        self.password = password
        #check against db here
        self.status = 'logged_in'
        return self.status

    
    def getPurchaseHistory(self):
        #access db for a list of items and put into itemList
        os.system('cls' if os.name == 'nt' else 'clear')
        print ('***********' + self.username + ' Purchase History ************')
        itemList = ['Hammer', 'Grapefruit', 'Boots', 'How to Use a Hammer by Pinky']
        i = 1
        for item in itemList:
            print (str(i) + '. ' + item + '    Date: 12/23/2016')
            i = i + 1
	
    
    def getUserAddress(self):
        return self.address

    
    def logout(self):
        self.username = ''
        self.password = ''
        self.address = ''
        self.status = 'not_logged_in'
		
    
    def getUserID(self):
        return self.username
