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
    print("OS Booting up")
    sleep(1.25)