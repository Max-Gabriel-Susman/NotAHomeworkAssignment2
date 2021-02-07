# Max Susman
# CS 1400 - L01
# Assignment 3

import math

# person one data collection
print("Person One")
nameOne = input("Enter your name : ")
positionOne = input("Enter your position : ")
radiusOne = input("Enter your personal space radius : ")

# person two data collection
print("Person Two")
nameTwo = input("Enter your name : ")
positionTwo = input("Enter your position : ")
radiusTwo = input("Enter your personal space radius : ")

# coordinate variables for positionOne are declared with empty strings
xOne = ""
yOne = ""
currentCoordinateIsX = True

# parsing positionOne
for char in positionOne:
    if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
        if currentCoordinateIsX:
            xOne += char
        else:
            yOne += char
    elif char == ",":
        currentCoordinateIsX = False
    else:
        continue

# coordinate variables for positionTwo are declared with empty strings
xTwo = ""
yTwo = ""
currentCoordinateIsX = True

# parsing positionTwo
for char in positionOne:
    if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
        if currentCoordinateIsX:
            xOne += char
        else:
            yOne += char
    elif char == ",":
        currentCoordinateIsX = False
    else:
        continue

# Test result variables are declared as empty strings
personTestResult = ""
spaceTestResult = ""
# personProximity = (((xTwo - xOne)^2)+((yTwo - yOne)^2))^-2 # delete this bad boi after testing
# distance between the two persons' positions is calculated
personProximity = math.sqrt((math.pow(int(xTwo - xOne),2) + math.pow(int(yTwo - yOne),2))+())
# Person Test logic - I gotta switch up the order of the conditions
if radiusOne <= personProximity and radiusTwo > personProximity:
    personTestResult = "Person One is in Person Two's personal space"
elif radiusOne <= personProximity and radiusTwo > personProximity:
    personTestResult = "Person Two is in Person One's personal space"
elif radiusOne <= personProximity and radiusTwo >= personProximity:
    personTestResult = "Person One and Person Two are in each other's personal space"
else:
    personTestResult = "Neither Person One nor Person Two is in the other's personal space"

# Space Test logic
if radiusOne + radiusTwo >= personProximity:
    spaceTestResult = "Person One and Person Two's personal spaces overlap"
elif radiusOne >= personProximity + radiusTwo:
    spaceTestResult = "Person One and Person Two's personal spaces do not overlap"
elif radiusOne + radiusTwo >= personProximity:
    spaceTestResult = "Person One's personal space is entirely inside Person Two's personal space"
else:
    spaceTestResult = "Person Two's personal space is entirely inside Person One's personal space"

# Test result console output
print("Social Situation Analysis Results")
print("Person Test: " + personTestResult)
print("Space Test: " + spaceTestResult)