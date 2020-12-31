# -------------------------------------------------------
# This file contains and defines the customer class.
# -------------------------------------------------------
# Author: ulku
# Version: BeerGame Vol1.4
# -------------------------------------------------------

from config import CUSTOMER_INITIAL_ORDERS, CUSTOMER_SUBSEQUENT_ORDERS

class Customer:

    def __init__(self):
        # Initializes the Customer object in its initial state.
        self.totalBeerReceived = 0
        return

    def RecieveFromRetailer(self, amountReceived):
        self.totalBeerReceived += amountReceived

        return

    def CalculateOrder(self, weekNum):
        # The customer orders 4 cases on weeks 1-5, and 8 cases
        # for all other weeks.
        if weekNum <= 5:
            result = CUSTOMER_INITIAL_ORDERS
        else:
            result = CUSTOMER_SUBSEQUENT_ORDERS
        return result

    def GetBeerReceived(self):
        return self.totalBeerReceived