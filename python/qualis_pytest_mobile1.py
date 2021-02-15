# Pytest 
# Mobile

class InsufficientException(Exception):
    pass
 
 
class MobileInventory:
    def __init__(self, inventory={}):
        if type(inventory) != dict:
            raise TypeError("Input inventory must be a dictionary")
        elif inventory == {}:
            self.balanced_inventory = inventory
        elif inventory != {}:
            for i in inventory.keys():
                if type(i) != str:
                    raise ValueError("Mobile model name must be a string")
            for i in inventory.values():
                if type(i) != int or i < 0:
                    raise ValueError("No. of mobiles must be a positive integer")
            self.balanced_inventory = inventory
 
    def add_stock(self, new_stock):
        if type(new_stock) != dict:
            raise TypeError("Input stock must be a dictionary")
        elif new_stock != {}:
            for i in new_stock.keys():
                if type(i) != str:
                    raise ValueError("Mobile model name must be a string")
            for i in new_stock.values():
                if type(i) != int or i < 0:
                    raise ValueError("No. of mobiles must be a positive integer")
            self.balanced_inventory.update(new_stock)
 
    def sell_stock(self, requested_stock):
        if type(requested_stock) != dict:
            raise TypeError("Input stock must be a dictionary")
        elif requested_stock != {}:
            mobileName = []
            mobileQuantity = []
            for i in requested_stock.keys():
                if type(i) != str:
                    raise ValueError("Mobile model name must be a string")
            for i in requested_stock.values():
                if type(i) != int or i < 0:
                    raise ValueError("No. of mobiles must be a positive integer")
            for i in requested_stock.keys():
                if i not in self.balanced_inventory.keys():
                    raise InsufficientException("No Stock. New Model Request")
                if self.balanced_inventory[i] < requested_stock[i]:
                    raise InsufficientException("Insufficient Stock")
                else:
                    self.balanced_inventory[i] = (
                        self.balanced_inventory[i] - requested_stock[i]
                    )
