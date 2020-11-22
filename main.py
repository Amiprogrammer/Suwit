import os
import random

# the command of color in window cmd
green = "color a"
red = "color 4"
white = "color 7"
ligth_red = "color c"
color = white

program_running = True
while program_running:
    try:
        print("""
x====xxxx===x
=x= SUWIT =x=
==x==xxx==x==

pili sala satuh:
* guntin
* batu
* kertas
*
* keluar atauh q
""") 

        computer = random.choice(["batu","guntin","kertas"])
        player = str(input("ketik disini: "))
        
        # if user want to close the program
        if player.lower() == "keluar" or player.lower() == "q":
            program_running = False

    except Exception as error:
        print(error)