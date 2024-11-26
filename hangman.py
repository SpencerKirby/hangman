"""
Spencer Kirby 
Self explanitory program its hangman, everyone knows how to play hangman 
"""
import random

def choose_word():
    # List of words to choose from add whatever words you want  
    words = ["jazz"]#jazz is a goated hangman word btw 
    return random.choice(words)

def display(word, guessed):#displays word based of past guesses 
    ret = ""
    for letter in word:
        if letter in guessed:
            ret += letter
        else:
            ret += "_"
    return ret

def runner():#runner 
    
    word = choose_word()
    guessed = []  
    attempts = 6  #amount of attempts given to player 
    wrong = []  
    while attempts > 0:#main loop 
        print("\nWord to guess: " + display(word, guessed))
        
        print("Guessed letters: " + ", ".join(guessed))
        print(f"Wrong guesses: " + ", ".join(wrong))
        
        print(f"Attempts remaining: {attempts}")
        
        guess = input("Enter a letter: ").lower()

        if guess in guessed or guess in wrong:
            print("You've already guessed that letter.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("invalid.")
            continue
        
        if guess in word:
            print(f"good {guess} is in the word.")
            guessed.append(guess)
        else:
            print(f"wrong {guess} is not in the word.")
            wrong.append(guess)
            attempts -= 1
        
        if set(word) == set(guessed):
            print(f"you win: {word}")
            break
    
    if attempts == 0:
        print(f"\nyou lost, word was  {word}")

runner()
