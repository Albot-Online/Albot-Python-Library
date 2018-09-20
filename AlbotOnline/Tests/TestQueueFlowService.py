from AlbotOnline.QueueFlowServiceControl.Simulation import *
import random

'''
To install Albot.Online you can use the "pip install Albot.Online" command.
Make sure the installed version is 0.60 or later.

Simply define some constants and start creating the logic for the flow & service controller.
A simulation is locked contained within an instances, this allows for easy multithreading if needed.

After every tick you will be returned the a object describing the current state of the simulation.

Currently the costs are simply the exact values entered.
This also goes for the "WaitCost" which is just the current number of jobs in the queue. 
Although this is specified to be a increasing convex function. This can be easily altered later.
'''


#Random choosen consts
A_MIN = 0.2; A_MAX = 0.8; B_MIN = 0.1; B_MAX = 0.9
QUEUE_SIZE = 100


#Do some clever decision making here. Instead of a random decision
def flowControl(queue, queueSize, bMin, bMax):
    return bMax if random.random() > 0.5 else bMin

#Do some clever decision making here. Instead of a random decision
def serviceControl(queue, queueSize, aMin, aMax):
    return aMin if random.random() > 0.5 else aMax


#Instansiate a version of the simulator
sim = Simulation(queueSize=QUEUE_SIZE, aMin=A_MIN, aMax=A_MAX, bMin=B_MIN, bMax=B_MAX,
                 flowControl=flowControl, serviceControl=serviceControl
                 )


for i in range(100):
    postState = sim.tick()

    print("***********")
    print("Round: ", i)
    print("Wait Cost:", postState.totalWaitCost)
    print("Flow Cost:", postState.totalFlowCost)
    print("Service Cost:", postState.totalServiceCost)
    print("Objects in Queue:", postState.currentQueue)
    print("Queue Size:", postState.queueSize)