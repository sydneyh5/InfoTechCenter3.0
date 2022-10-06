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
#to rsndomly choose a condition and storing it in it's brain
def weather():
    weatherForcast = ["Rain", "Snow", "Sunny", "Cloudy", "Foggy", "Storming", "Icy"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

