"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Alexandr Nosek 
email: alexandr.nosek51@gmail.com
discord: Alex Nosek  Vintag
"""

import random

#pozdrav
def greetings():
    separator = "-" * 47
    print(f"Hi there!\n {separator}")
    print(f"I've generated a random 4 digit number for you.\n Lets play a bulls and cows game.\n{separator}")


def generated_number(): #ošetřit na duplicity.. tuple
    return str(random.randrange(1111, 9999))
    



def game():
    greetings()
    game_running = True
    target_number = generated_number()
    print(target_number)
    while game_running:
        users_number = input("Enter the 4-digit number: ")
        if len(users_number) != 4 or not users_number.isdigit():
            print("You've entered the wrong line!")
            continue
        elif users_number == target_number:
            print("Congratulation!")
            game_running = False
        target_number = [num for num in target_number]
        print(target_number)
        bulls = []
        for number in users_number:#zjištění na počet bulls 
            if number == target_number[0] or number == target_number[1] or number == target_number[2] or number == target_number[3]:
                bulls.append(number)
                
            
        print(len(bulls))
        




        

game()

