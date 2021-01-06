# This file contains and defines the SupplyChainStatistics class.

import matplotlib.pyplot as plt

class SupplyChainStatistics:

    def __init__(self):

        #Cost statistics
        self.retailerCostsOverTime = []
        self.wholesalerCostsOverTime = []
        self.distributorCostsOverTime = []
        self.factoryCostsOverTime = []

        #Order statistics
        self.retailerOrdersOverTime = []
        self.wholesalerOrdersOverTime = []
        self.distributorOrdersOverTime = []
        self.factoryOrdersOverTime = []

        #Effective inventory statistics
        self.retailerEffectiveInventoryOverTime = []
        self.wholesalerEffectiveInventoryOverTime = []
        self.distributorEffectiveInventoryOverTime = []
        self.factoryEffectiveInventoryOverTime = []

        return


    def RecordRetailerOrders(self, retailerOrdersThisWeek):
        # retailerOrdersThisWeek is appended to
        # retailerOrdersOverTime, a list which tracks the retailer's
        # weekly orders.
        self.retailerOrdersOverTime.append(retailerOrdersThisWeek)
        return


    def RecordWholesalerOrders(self, wholesalerOrdersThisWeek):
        self.wholesalerOrdersOverTime.append(wholesalerOrdersThisWeek)
        return


    def RecordDistributorOrders(self, distributorOrdersThisWeek):

        self.distributorOrdersOverTime.append(distributorOrdersThisWeek)
        return


    def RecordFactoryOrders(self, factoryOrdersThisWeek):
        self.factoryOrdersOverTime.append(factoryOrdersThisWeek)
        return


    def RecordRetailerCost(self, retailerCostsThisWeek):
        self.retailerCostsOverTime.append(retailerCostsThisWeek)
        return


    def RecordWholesalerCost(self, wholesalerCostsThisWeek):
        self.wholesalerCostsOverTime.append(wholesalerCostsThisWeek)
        return


    def RecordDistributorCost(self, distributorCostsThisWeek):
        self.distributorCostsOverTime.append(distributorCostsThisWeek)
        return


    def RecordFactoryCost(self, factoryCostsThisWeek):
        self.factoryCostsOverTime.append(factoryCostsThisWeek)
        return


    def RecordRetailerEffectiveInventory(self, retailerEffectiveInventoryThisWeek):
        self.retailerEffectiveInventoryOverTime.append(retailerEffectiveInventoryThisWeek)
        return


    def RecordWholesalerEffectiveInventory(self, wholesalerEffectiveInventoryThisWeek):
        self.wholesalerEffectiveInventoryOverTime.append(wholesalerEffectiveInventoryThisWeek)
        return


    def RecordDistributorEffectiveInventory(self, distributorEffectiveInventoryThisWeek):
        self.distributorEffectiveInventoryOverTime.append(distributorEffectiveInventoryThisWeek)
        return


    def RecordFactoryEffectiveInventory(self, factoryEffectiveInventoryThisWeek):
        self.factoryEffectiveInventoryOverTime.append(factoryEffectiveInventoryThisWeek)
        return


    def PlotCosts(self):
        plt.title("Cost Incurred Over Time")
        plt.plot(self.retailerCostsOverTime, "r", label = "Retailer")
        plt.plot(self.wholesalerCostsOverTime, "g", label = "Wholesaler")
        plt.plot(self.distributorCostsOverTime, "b", label = "Distributor")
        plt.plot(self.factoryCostsOverTime, "m", label="Factory")
        plt.legend(loc='upper left', shadow=True)
        plt.ylabel('Cost ($)')
        plt.xlabel("Weeks")
        plt.show()

        return


    def PlotOrders(self):
        plt.title("Orders Placed Over Time")
        plt.plot(self.retailerOrdersOverTime, "r", label = "Retailer")
        plt.plot(self.wholesalerOrdersOverTime, "g", label = "Wholesaler")
        plt.plot(self.distributorOrdersOverTime, "b", label = "Distributor")
        plt.plot(self.factoryOrdersOverTime, "m", label="Factory")
        plt.legend(loc='upper left', shadow=True)
        plt.ylabel('Orders')
        plt.xlabel("Weeks")
        plt.show()

        return


    def PlotEffectiveInventory(self):
        plt.title("Effective Inventory Over Time")
        plt.plot(self.retailerEffectiveInventoryOverTime, "r", label = "Retailer")
        plt.plot(self.wholesalerEffectiveInventoryOverTime, "g", label = "Wholesaler")
        plt.plot(self.distributorEffectiveInventoryOverTime, "b", label = "Distributor")
        plt.plot(self.factoryEffectiveInventoryOverTime, "m", label="Factory")
        plt.legend(loc='upper left', shadow=True)
        plt.ylabel('Effective Inventory')
        plt.xlabel("Weeks")
        plt.show()

        return
