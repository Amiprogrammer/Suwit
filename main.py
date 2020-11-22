import os
import random

# the command of color in window cmd
green = "color a"
red = "color 4"
white = "color 7"
ligth_red = "color c"

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
* keluar (q)
""") 

        computer = random.choice(["batu","guntin","kertas"])
        player = str(input("ketik disini: "))
        break
    except Exception as error:
        print(error)