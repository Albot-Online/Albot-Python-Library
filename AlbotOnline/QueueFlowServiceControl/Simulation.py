import random
import numpy as np

class Simulation:

    def __init__(self, queueSize, aMin, aMax, bMin, bMax):
        self.queueSize = int(queueSize)
        self.queue = 0
        self.flowCost = 0
        self.serviceCost = 0
        self.waitCost = 0
        self.completedJobs = 0

        self.aMin = aMin
        self.aMax = aMax
        self.bMin = bMin
        self.bMax = bMax

    def tick(self, flowControl, serviceControl):
        if(self._canAddMoreJobs()):
            B = flowControl(self.queue, self.queueSize, self.bMin, self.bMax)
            self._addFlowCost(B)
            self._addJobb(B)

        self._addCurrentWaitCost()
        if(self._canServeJobs()):
            A = serviceControl(self.queue, self.queueSize, self.aMin, self.aMax)
            self._addServiceCost(A)
            self._serveJob(A)

        return self.getStateVector(B, A)


    def getStateVector(self, immediateFlowCost, immediateServiceCost):
        vec = lambda: None
        vec.totalWaitTime = self.waitCost
        vec.totalFlowCost = self.flowCost
        vec.totalServiceCost = self.serviceCost

        vec.immWaitCost = self.currentWCost
        vec.immFlowPower = immediateFlowCost
        vec.immServicePower = immediateServiceCost

        vec.completedJobs = self.completedJobs
        vec.currentQueue = self.queue
        vec.queueSize = self.queueSize
        return vec

    def _addCurrentWaitCost(self):
        self.currentWCost = self.queue
        self.waitCost += self.queue

    #Flow Controller
    def _canAddMoreJobs(self):
        return self.queue < self.queueSize

    def _addJobb(self, B):
        if(random.random() >= B):
            self.queue += 1

    def _addFlowCost(self, B):
        self.flowCost += B



    #Service Controller
    def _canServeJobs(self):
        return self.queue > 0

    def _serveJob(self, A):
        if(random.random() >= A):
            self.queue -= 1
            self.completedJobs += 1

    def _addServiceCost(self, A):
        self.serviceCost += A