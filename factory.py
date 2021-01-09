from Settings import (CUSTOMER_INITIAL_ORDERS, TARGET_STOCK)
from SupplyChainActor import SupplyChainActor
from SupplyChainQueue import SupplyChainQueue

class Factory(SupplyChainActor):

    def __init__(self, incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue, productionDelayWeeks):
        # Initializes the Factory object in its initial state
        # by calling parent constructor and setting the
        # retailer's customer.
        super().__init__(incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue)
        self.BeerProductionDelayQueue = SupplyChainQueue(productionDelayWeeks)

        #We assume that the factory already has some runs in production. This is in the rules, and ensures initial stability.
        self.BeerProductionDelayQueue.PushEnvelope(CUSTOMER_INITIAL_ORDERS)
        self.BeerProductionDelayQueue.PushEnvelope(CUSTOMER_INITIAL_ORDERS)
        return

    def ProduceBeer(self, weekNum):
        if weekNum <= 4:
            amountToOrder = 4
        #After first few weeks, the actor chooses the order. We use "anchor and maintain" strategy.
        else:
            #We want to cover any outflows
            amountToOrder = 0.5 * self.currentOrders

            if (TARGET_STOCK - self.currentStock) > 0:
                amountToOrder += TARGET_STOCK - self.currentStock

        self.BeerProductionDelayQueue.PushEnvelope(amountToOrder)
        self.lastOrderQuantity = amountToOrder

        return

    def FinishProduction(self):
        # Updates currentStock to reflect the beer
        # that the factory just brewed.
        # -------------------------------------------------------
        amountProduced = self.BeerProductionDelayQueue.PopEnvelope()

        if amountProduced > 0:
            self.currentStock += amountProduced

        return

    def TakeTurn(self, weekNum):
        #The steps for taking a turn are as follows:

        #PREVIOUS PRODUCTION RUNS FINISH BREWING.
        self.FinishProduction()

        #RECEIVE NEW ORDER FROM DISTRIBUTOR
        self.ReceiveIncomingOrders()     #This also advances the queue!

        #PREPARE DELIVERY
        if weekNum <= 4:
            self.PlaceOutgoingDelivery(4)
        else:
            self.PlaceOutgoingDelivery(self.CalcBeerToDeliver())

        #PRODUCE BEER
        self.ProduceBeer(weekNum)

        #UPDATE COSTS
        self.costsIncurred += self.CalcCostForTurn()

        return
