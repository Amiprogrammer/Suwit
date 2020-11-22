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

        # logic to winner or loser
        if computer == "batu" and player.lower() == "kertas":
            print("kamu menan!")
            print("===========")
            print('"komputer": memilih batu\n"kamu": memilih kertas')
        elif computer == "guntin" and player.lower() == "batu":
            print("kamu menan!")
            print("===========")
            print('"komputer": memilih guntin\n"kamu": memilih batu')
        elif computer == "kertas" and player.lower() == "guntin":
            print("kamu menan!")
            print("===========")
            print('"komputer": memilih kertas\n"kamu": memilih guntin')
        elif computer == "kertas" and player.lower() == "batu":
            print("kamu kalah!")
            print("===========")
            print('"komputer": memilih kertas\n"kamu": memilih batu')
        elif computer == "guntin" and player.lower() == "kertas":
            print("kamu kalah!")
            print("===========")
            print('"komputer": memilih guntin\n"kamu": memilih kertas')
        elif computer == "batu" and player.lower() == "guntin":
            print("kamu kalah!")
            print("===========")
            print('"komputer": memilih batu\n"kamu": memilih guntin')
        elif computer == player.lower():
            print("pilihan anda sama dengan komputer!")
        else:
            print("pilihan tidak ditemukan? coba lagi!")

    except Exception as error:
        print(error)