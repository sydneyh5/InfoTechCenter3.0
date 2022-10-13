#Gasoline
#Programmer: Sydney Hribar
#Version 1.0

"""
Define a function to check our gas gauge and determine how far
we have until we need gasoline based on an if, elif, else condition
"""

#Import library here
import random
from time import sleep

#Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Variable calling the gasLevelGauge function to store value once
gasLevelIndicator = gasLevelGauge()

def listOfGasStations():
    gasStations = ["Shell","Circle K","Marathon","Speedway","Meijer"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(26,50), 1)
    if gasLevelIndicator == "Empty":
        print("\033[1;31m***WARNING YOU ARE ON EMPTY***\033[0m")
        sleep(1.25)
        print("Calling Emergency Contact.")
    elif gasLevelIndicator == "Low":
        print("\033[1;31m***WARNING***\033[0m")
        sleep(1)
        print("Your gas level is extremely low, checking google maps for the closest gas station.")
        sleep(1)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("\033[1;31m***WARNING***\033[0m")
        sleep(1)
        print("Your gas level is at a quarter tank, checking google maps for the closest gas station.")
        sleep(1)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationQuarterTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas level is at half tank, you won't need gas for a little while.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas level is at three quarters tank, you have plenty of gas to get where you are going.")
    else:
        print("\033[1;32mYour gas tank is full, you have plenty of gas to get where you are going.")



gasLevelAlert()