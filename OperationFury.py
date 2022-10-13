
#****************************************************************************************
#Import Libraries Here
from time import sleep #We imported the Sleep function from the Time library

import random
#****************************************************************************************

#Welcome Screen
#Developer: Sydney Hribar
#Version: 1.1

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTechCenter OS is loading
"""

#To change the color of the text out put \033[1;32m and change the last number to change
#The text color
#To reset the color use \033[0m


print("\n\033[1;36mWelcome to Operation Fury InfoTech Center")
sleep(2)
print("\n\033[1;34mOperation Fury's Operating System is Booting up\033[0m")

for i in range(3):
    print("\033[1;35mOS Booting up\033[0m")
    sleep(1.25)

#****************************************************************************************

#Weather
#Developer
#Version 1.0

"""
Create a function for our current weather using the
ramdom.choice function to determine what the weather
is picking from a list - using If, elif, and else statements
to check the condition and print a specific print line
"""


#Weather Condition list using the random.choice library
#to randomly choose a condition and storing it in it's brain
def weather():
    weatherForcast = ["Rain", "Snow", "Sunny", "Windy", "Foggy", "Storming", "Icy"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Icy":
        print("\nVRS has changed your Alarm 30 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 30MPH\n")
    elif weatherAlert == "Snow":
        print("\nVRS has changed your Alarm 15 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 50MPH\n")
    elif weatherAlert == "Rain":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 60MPH\n")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 70MPH\n")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 65MPH\n")
    elif weatherAlert == "Storming":
        print("\nVRS has changed your Alarm 15 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 50MPH\n")
    else:
        print("\nThe weather today is",weatherAlert)
        print("VRS will allow your car to go 95MPH\n")

#****************************************************************************************

#Gasoline
#Programmer: Sydney Hribar
#Version 1.0

"""
Define a function to check our gas gauge and determine how far
we have until we need gasoline based on an if, elif, else condition
"""


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


#****************************************************************************************

#Call functions here...
print()
gasLevelAlert()
vehicleResponseSystem()