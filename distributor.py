# -------------------------------------------------------
# This file contains and defines the Distributor class.
# -------------------------------------------------------

from supplyChainActor import SupplyChainActor

class Distributor(SupplyChainActor):

    def __init__(self, incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue):
        # Initializes the Distributor object in its initial state
        # by calling parent constructor.
        super().__init__(incomingOrdersQueue, outgoingOrdersQueue,
                         incomingDeliveriesQueue, outgoingDeliveriesQueue)
        return


    def TakeTurn(self, weekNum):
        #The steps for taking a turn are as follows:

        #RECEIVE NEW DELIVERY FROM FACTORY
        self.ReceiveIncomingDelivery()    #This also advances the queue!

        #RECEIVE NEW ORDER FROM WHOLESALER
        self.ReceiveIncomingOrders()     #This also advances the queue!

        #PREPARE DELIVERY
        if weekNum <= 4:
            self.PlaceOutgoingDelivery(4)
        else:
            self.PlaceOutgoingDelivery(self.CalcBeerToDeliver())

        #PLACE ORDER
        self.PlaceOutgoingOrder(weekNum)

        #UPDATE COSTS
        self.costsIncurred += self.CalcCostForTurn()

        return