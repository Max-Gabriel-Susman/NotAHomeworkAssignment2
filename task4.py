# Max Susman
# CS 1400 - L01
# Assignment 3

import math

# stores boolean that is used to terminate runtime loop
simulationQueued = True

# runtime loop
while simulationQueued:

    # counter used to count the number of samples in the current test pool
    sampleCounter = 0

    # counters used to store zookeepers data
    noElephantsFoundCounter = 0
    oneElephantFoundCounter = 0
    twoElephantsFoundCounter = 0

    # test pool loop
    while sampleCounter < 100000:
        # pseudo random numbers will detemine what pen each elephant is sleeping in
        elephantAPen = math.randint(1, 7)
        elephantBPen = math.randint(1, 7)
        penChecked = math.randint(1, 7)

        # logic used to determine instance's result
        if elephantAPen == elephantBPen and elephantBPen == penChecked:
            twoElephantsFoundCounter += 1
        elif elephantAPen == penChecked or elephantBPen == penChecked:
            oneElephantFoundCounter += 1
        else:
            noElephantsFoundCounter += 1



    # we need to report the following statistics
    # what percentage of time is their at least one elephant in the pen the zookeeper checks?
    # what percentage of time is their two elephants in the pen that the zookeeper checks
    print("The percentage of time there was at least one elephant in the pen checked by the zookeeper was ")

    # boolean used to terminate encore loop
    waitingOnInput = True

    # encore loop runs until valid input is received
    while waitingOnInput:
        encore = input("Run the simulation again? (yes or no): ")

        # logic for validating encore's input
        if encore == "yes":
            waitingOnInput = False
        elif encore == "no":
            simulationQueued = False
            waitingOnInput = False
        else:
            print("Invalid input, just give me a \"yes\" or a \"no\" this time, thanks.")

