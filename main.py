import random
import hangman_words
import hangman_art
#from replit import clear

#Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.
print("We welcome you to this game of Hangman!")
print(hangman_art.logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in chosen_word:
  display.append("_")

#Check guessed letter
while "_" in display:
    guess = input("Guess a letter: ").lower()
    #After every guess, the screen clears
    #clear()
    #If guess is not a letter in the chosen_word,
    if guess not in chosen_word:
        #Then reduce 'lives' by 1. 
        lives -= 1
        print(f"You have guessed '{guess}'. That's not in the word. You are close to losing. You have {lives} lives remaining!")
        #Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
        print(hangman_art.stages[lives])
        #If lives goes down to 0 then the game should stop and it should print "You lose."
        if lives == 0:
            print("You lost. We're sad T_T")
            print(f"The chosen word was '{chosen_word}'!.")
            break
    elif guess in chosen_word:
        #If the user has entered a letter they've already guessed, print the letter and let them know.
        if guess in display:
            print("You have already made this guess. Try some other letter!")
        for letter in chosen_word: 
            if letter == guess: 
                    for i in range(len(display)): 
                        if chosen_word[i] == guess: 
                            display[i] = guess 
        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")
    
#Check if user has got all letters.
if "_" not in display:
    print("You win! ^_^")
