# Max Susman
# CS 1400 - L01
# Assignment 3

import math
import random

# stores boolean that is used to terminate runtime loop
simulationQueued = True

testPoolSize = 100000

# poorly written comedic relief
print("Welcome to Elephant Simulator 5000")

# runtime loop
while simulationQueued:

    # counter used to count the number of samples in the current test pool
    sampleCounter = 0

    # counters used to store zookeepers data
    noElephantsFoundCounter = 0
    oneElephantFoundCounter = 0
    twoElephantsFoundCounter = 0

    # test pool loop
    while sampleCounter < testPoolSize:
        # pseudo random numbers will detemine what pen each elephant is sleeping in
        elephantAPen = random.randint(1, 6)
        elephantBPen = random.randint(1, 6)
        penChecked = random.randint(1, 6)

        # logic used to determine instance's result
        if elephantAPen == elephantBPen and elephantBPen == penChecked:
            twoElephantsFoundCounter += 1
        elif elephantAPen == penChecked or elephantBPen == penChecked:
            oneElephantFoundCounter += 1
        else:
            noElephantsFoundCounter += 1

        print(str(sampleCounter + 1) + "th sample collected")
        sampleCounter += 1

    # these variables store the statistics derived from the testing pool
    percentSingleElephantFound = oneElephantFoundCounter / testPoolSize
    percentTwoElephantsFound = twoElephantsFoundCounter / testPoolSize

    # this is just for debug, remove for submission
    print(oneElephantFoundCounter)
    print(twoElephantsFoundCounter)

    # we need to report the following statistics
    # what percentage of time is their at least one elephant in the pen the zookeeper checks?
    # what percentage of time is their two elephants in the pen that the zookeeper checks
    print("The percentage of time there was at least one elephant in the pen checked by the zookeeper was " + str(oneElephantFoundCounter) + "%.")
    print("The percentage of time there was at least one elephant in the pen checked by the zookeeper was " + str(twoElephantsFoundCounter) + "%.")
    print("The zookeeper was incorrect")
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

