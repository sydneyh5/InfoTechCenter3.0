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

def gasLevelAlert():
    if gasLevelIndicator == "Empty":
        print("\033[1;31m***WARNING YOU ARE ON EMPTY***\033[0m")
        sleep(1.25)
        print("Calling Emergency Contact")

gasLevelAlert()