#File location of hang man word list which we will need to scrape a random word from at the start of our program
#This location can be anywhere, and your location will be different than mine so update accordingly
#D:\CodeClicks\code\gameData\hangManWordList.txt

#library we will need
import random

# Stick figure stages
#file for stick figure will be down below in comments
stick_figure = [
    """
     _________
     |/      |
     |      
     |     
     |     
     |      
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |      
     |      
     |      
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |       |
     |      
     |      
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
    """,
    """
     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
    """
]

#Let us first create a helper function
def get_random_word():
    with open("D:\CodeClicks\code\gameData\hangManWordList.txt", "r") as file:
        words = file.readlines()
    return random.choice(words).strip() #helps to remove the newline character


#Let us now create the game
def hangman():
    word = get_random_word()
    word_letters = list(word)
    guessed_letters = []
    inncorrect_guesses = 0

    while inncorrect_guesses < len(stick_figure):
        #Display the current state of the word
        display_word = ""

        for letter in word_letters:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "-"
        
        print(display_word)

        if display_word == word:
            print("Congratulations! You guessed the word.")
            break

        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try another guess.")
            
            elif guess in word_letters:
                print("That guess was correct!")
                guessed_letters.append(guess)
            
            else:
                print("You guessed wrong!")
                inncorrect_guesses +=1
                print("Tries remaining:", len(stick_figure) - inncorrect_guesses)
                print(stick_figure[inncorrect_guesses - 1])
                guessed_letters.append(guess)
                
                if inncorrect_guesses == len(stick_figure):
                    print("You ran out of tries. The word was: ", word)

        else:
            print("Invalid input. Please enter a single letter.")
hangman()
