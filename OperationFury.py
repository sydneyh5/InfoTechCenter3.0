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
    if gasLevelIndicator == "Empty":
        print("\033[1;31m***WARNING YOU ARE ON EMPTY***\033[0m")
        sleep(1.25)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("\033[1;31m***WARNING***\033[0m")
        sleep(1)
        print("Your gas level is extremely low, checking google maps for the closest gas station")
        sleep(1)
        print("The closest gas station is",listOfGasStations())

gasLevelAlert()