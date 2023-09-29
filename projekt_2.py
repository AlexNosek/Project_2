import random

"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Alexandr Nosek
email: alexandr.nosek51@gmail.com
discord: Vintag, Alex Nosek
"""
separator = "-" * 47

def greetings():
    print(f"Hi there! Lets play Bulls and Cows\n{separator}")

def generating_number() -> list:
    '''
    Generates and returns a unique 4-digit number in the list
    '''
    print(f"I've generated a random 4 digit number for you.\n{separator}")
    generated_number = random.sample(range(1, 10), 4)  
    generated_number = [str(digit) for digit in generated_number]  
    return generated_number

def guessing_number(generated_number) -> int:
    tries = 0
    while True:
        tries += 1
        bulls = 0
        cows = 0
        user_input = list(input("Enter a 4-digit number: "))
        if len(user_input) != 4 or user_input[0] == "0" or len(set(user_input)) != 4:
            print("User input must always contain 4 digits, must not be duplicated and must not start with zero")
            continue
        elif user_input == generated_number:
            print(f"Correct, you've guessed the right number in {tries} guesses!")
            break
        for number1, number2 in zip(user_input, generated_number):
            if number1 == number2:
                bulls += 1
            elif number1 in generated_number:
                cows += 1
        if (bulls == 1 or cows == 1):
            print(f"{bulls} bull {cows} cow --> Tries : {tries}\n{separator}")
        else:
            print(f"{bulls} bulls {cows} cows--> Tries : {tries}\n{separator}")
    return tries

def result_of_game(tries : int):
    if tries >= 1 and tries <= 7:
        print("Excellent result!")
    elif tries >= 8 and tries <= 15:
        print("Good result!")
    else:
        print("It could be better, lets try again")


def play_again():
    while True:
        game_reset = input("If you wanna play again, press Y, otherwise, press N: ").lower()
        if game_reset == "y":
            break
        elif game_reset == "n":
            exit()
        else:
            print("You have pressed the wrong character!")
            continue



def main():
    #pozdrav
    greetings()
    #vygenerování čísla
    generated_number = generating_number()
    #vyhodnocení uživatelského čísla
    game = guessing_number(generated_number)
    #podle počtu pokusů
    result_of_game(game)
    #hrát znova?
    play_again()




main()

if __name__ == "__main__":
    main()