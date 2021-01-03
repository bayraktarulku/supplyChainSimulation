# This file contains and defines the SupplyChainQueue class.
# The SupplyChainQueue consists of a two element list. Element
# 0 is the oldest order/delivery in the queue, and element 1
# is the second oldest order/delivery in the queue, etc. The
# queue length is limited by the queueLength parameter.



class SupplyChainQueue():

    def __init__(self, queueLength):
        self.queueLength = queueLength
        self.data = []

        return


    def PushEnvelope(self, numberOfCasesToOrder):
        orderSuccessfullyPlaced = False

        if len(self.data) < self.queueLength:
            self.data.append(numberOfCasesToOrder)
            orderSuccessfullyPlaced = True

        return orderSuccessfullyPlaced


    def AdvanceQueue(self):
        self.data.pop(0)

        return


    def PopEnvelope(self):
        if len(self.data) >= 1:
            quantityDelivered = self.data[0]
            self.AdvanceQueue()
        else:
            quantityDelivered = 0

        return quantityDelivered


    def PrettyPrint(self):
        print(self.data)
        return
