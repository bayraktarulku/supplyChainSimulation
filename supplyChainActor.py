# This file contains and defines the supplyChainActor class.

from Settings import (INITIAL_STOCK, INITIAL_CURRENT_ORDERS,
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