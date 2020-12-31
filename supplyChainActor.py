# This file contains and defines the supplyChainActor class.

from config import (INITIAL_STOCK, INITIAL_CURRENT_ORDERS,
                      INITIAL_COST, TARGET_STOCK, STORAGE_COST_PER_UNIT,
                      BACKORDER_PENALTY_COST_PER_UNIT)

class SupplyChainActor:

    def __init__(self, incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue):
        self.currentStock = INITIAL_STOCK
        self.currentOrders = INITIAL_CURRENT_ORDERS
        self.costsIncurred = INITIAL_COST

        self.incomingOrdersQueue = incomingOrdersQueue
        self.outgoingOrdersQueue = outgoingOrdersQueue
        self.incomingDeliveriesQueue = incomingDeliveriesQueue
        self.outgoingDeliveriesQueue = outgoingDeliveriesQueue

        self.lastOrderQuantity = 0

        return



    def PlaceOutgoingDelivery(self, amountToDeliver):
        self.outgoingDeliveriesQueue.PushEnvelope(amountToDeliver)
        return


    def PlaceOutgoingOrder(self, weekNum):
        # Calculates the order quantity using an anchor and maintain
        # strategy.

        #First weeks are in equilibrium
        if weekNum <= 4:
            amountToOrder = 4
        #After first few weeks, the actor chooses the order. We use "anchor and maintain" strategy.
        else:
            #We want to cover any out flows, we know that there are some orders in the pipeline.
            amountToOrder = 0.5 * self.currentOrders

            if (TARGET_STOCK - self.currentStock) > 0:
                amountToOrder += TARGET_STOCK - self.currentStock

        self.outgoingOrdersQueue.PushEnvelope(amountToOrder)
        self.lastOrderQuantity = amountToOrder

        return


    def ReceiveIncomingDelivery(self):
        # Updates the current stock based on the incoming
        # deliveries queue.
        quantityReceived = self.incomingDeliveriesQueue.PopEnvelope()

        if quantityReceived > 0:
            self.currentStock += quantityReceived

        return


    def ReceiveIncomingOrders(self):
        # Updates the current orders based on the incoming
        # deliveries queue.
        thisOrder = self.incomingOrdersQueue.PopEnvelope()

        if thisOrder > 0:
            self.currentOrders += thisOrder
        return


    def CalcBeerToDeliver(self):
        # Returns deliveryQuantitiy - the number of cases to be delivered

        # to the customer. currentOrders, currentStock are
        # updated to reflect this delivery quantity.

        deliveryQuantity = 0
         #If we can fill the customer's order, we must do it.
        if self.currentStock >= self.currentOrders:
            deliveryQuantity = self.currentOrders
            self.currentStock -= deliveryQuantity
            self.currentOrders -= deliveryQuantity
        #If the current stock cannot cover the order, we must fill as much as we can, and back-order the rest.
        elif self.currentStock >= 0 and self.currentStock < self.currentOrders:
            deliveryQuantity = self.currentStock
            self.currentStock = 0
            self.currentOrders -= deliveryQuantity

        return deliveryQuantity


    def CalcCostForTurn(self):
        # Returns costsThisTurn - the total cost incurred during

        # this turn.
        costsThisTurn = 0

        inventoryStorageCost = self.currentStock * STORAGE_COST_PER_UNIT
        backorderPenaltyCost = self.currentOrders * BACKORDER_PENALTY_COST_PER_UNIT

        costsThisTurn = inventoryStorageCost + backorderPenaltyCost

        return costsThisTurn


    def GetCostIncurred(self):
        return self.costsIncurred


    def GetLastOrderQuantity(self):
        return self.lastOrderQuantity


    def CalcEffectiveInventory(self):
        # Returns the effective inventory, which

        # is defined as self.currentStock - self.currentOrders.
        return (self.currentStock - self.currentOrders)