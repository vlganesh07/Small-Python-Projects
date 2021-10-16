import random 

NUM_DIGITS = 3 
MAX_GUESSES = 10 

def main():
    print('''Bages, a deductive logic game.
    
    I am thinking of a {}-digit number with no repeated digits. 
    Try to guess what it is Here are some clues
    when I say:      That means:
    Pico             One digit is correct but in the wrong position
    Fermi            One digit is correct and in the right position
    Bagels           No digit is correct
    
    For example if the secret was 248 and your guess was 843 the clues would 
    be Fermi Pico'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print("I have thought up a number")
        print("You have {} gusesses to get it ".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            #Keep looping until they enter a valid guess
            