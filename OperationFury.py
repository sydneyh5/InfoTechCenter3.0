
#Welcome Screen
#Developer: Sydney Hribar
#Version: 1.1

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTechCenter OS is loading
"""

#Import Libraries Here
from time import sleep #We imported the Sleep function from the Time library

#To change the color of the text out put \033[1;32m and change the last number to change
#The text color
#To reset the color use \033[0m


print("\n\033[1;36mWelcome to Operation Fury InfoTech Center")
sleep(2)
print("\n\033[1;34mOperation Fury's Operating System is Booting up\033[0m")

for i in range(3):
    print("\033[1;35mOS Booting up\033[0m")
    sleep(1.25)

#Weather
#Developer
#Version 1.0

"""
Create a function for our current weather using the
ramdom.choice function to determine what the weather
is picking from a list - using If, elif, and else statements
to check the condition and print a specific print line
"""

#Import Libraries here
import random

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
        print("VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snow":
        print("\nVRS has changed your Alarm 15 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Rain":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 70MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 65MPH")
    elif weatherAlert == "Storming":
        print("\nVRS has changed your Alarm 15 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    else:
        print("\nThe weather today is",weatherAlert)
        print("VRS will allow your car to go 95MPH")


vehicleResponseSystem()


