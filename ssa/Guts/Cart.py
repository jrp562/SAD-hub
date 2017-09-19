import os
from ssa.Guts.Item import Item

class Cart:
    def __init__(self, user):
        self.cartid = ''
        self.user = user
		self.cartItems = []

    def showItems(self):
        #get cart items from db and insert into list
        pass

    def purchaseCart(self):
        #prompt for address/creditcard
        #prompt for confirmation
        #put info and items into db
        pass
	
	def itemTotal(self):
		total = 0.0
		for each in cartItems:
			total += each.itemCost * each.itemQuantity
		
		print("$", total)
		
	
	def addItem(self, itemName):
		break
	
	def removeItem(self, itemName):
		break