# This file contains and defines the Retailer class.

from SupplyChainActor import SupplyChainActor

class Retailer(SupplyChainActor):

    def __init__(self, incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue, theCustomer):
        # Initializes the retailer object in its initial state
        # by calling parent constructor and setting the
        # retailer's customer.
        super().__init__(incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue)
        self.customer = theCustomer

        return

    def ReceiveIncomingOrderFromCustomer(self, weekNum):
        # Adds the customer's order to the current orders.
        self.currentOrders += self.customer.CalculateOrder(weekNum)
        return

    def ShipOutgoingDeliveryToCustomer(self):
        # Calculates the amount of beer to be delivered
        # based on the current stock. This is then added to the customer's
        # total beer received.
        self.customer.RecieveFromRetailer(self.CalcBeerToDeliver())
        return

    def TakeTurn(self, weekNum):
        #The steps for taking a turn are as follows:

        #RECEIVE NEW DELIVERY FROM WHOLESALER
        self.ReceiveIncomingDelivery()    #This also advances the queue!

        #RECEIVE NEW ORDER FROM CUSTOMER
        self.ReceiveIncomingOrderFromCustomer(weekNum)

        #CALCULATE AMOUNT TO BE SHIPPED, THEN SHIP IT
        #self.ShipOutgoingDeliveryToCustomer()
        if weekNum <= 4:
            self.customer.RecieveFromRetailer(4)
        else:
            self.customer.RecieveFromRetailer(self.CalcBeerToDeliver())

        #PLACE ORDER TO WHOLESALER
        self.PlaceOutgoingOrder(weekNum)

        #UPDATE COSTS
        self.costsIncurred += self.CalcCostForTurn()

        return
