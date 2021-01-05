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

    # def RecordFactoryCost(self, factoryCostsThisWeek):
        # pass
