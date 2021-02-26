
class WSMS:

    def __init__(self):
        self.inventory = {}

    def load_stock(self, filename):
        # Reads filename and adds contents to inventory
        self.filename = open(filename, 'r')
        for x in self.filename:
            self.bin.append(x)
        self.filename.close()

    def check_stock(self, item):
        # Returns the in stock quantity of an item
        self
        pass

    def add_stock(self, item, qty):
        # Increments the stock of the item by qty
        pass

    def remove_stock(self, item, qty):
        # Decrements the stock of the item by qty
        pass

    def pull_order(self, filename):
        # Reserves the order specified by filename
        # outputs the ordered bin pull list
        pass

    def fill_order(self, filename):
        # Deletes the specified pull list from the system
        pass

    def restock_order(self, filename):
        # Reads the given pull list to reverse the order
        # Deletes the pull list from the system
        pass

    def print_stock(self):
        # Prints the stock of each bin
        pass