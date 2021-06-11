word_to_guess = input("Please pick a word to guess...") # user inputs a word to guess
max_lives = 5    # max lives that the guesser has
wrong_counter = 1    # tracks the number of times the guesser guesses wrong
underscores = "________________________________________________________________________"   # this is used to make the initial hidden word
hidden_word = underscores[0:len(word_to_guess)]   # this creates the hidden word (e.g. "_____" for "Hello")
print(hidden_word)
incorrect_letters = []


# This function reveals a letter in the hidden word...
# this function has 3 arguments, the guessed letter, the word to guess and the hidden word (e.g. "h_ll_")
# it then converts the hidden word to a list and loops through the actual word to find
# out when the guessed letter appears,this information is stored in the counter variable,
# which is then used to swap an underscore in that position, to the guessed letter
# e.g. reveal_letter("e", "Hello", "_____") -> "_e___"
def reveal_letter(letter_picked, word_to_guess, underscored_word):
    counter = 0
    hidden_word_list = list(underscored_word)
    for letter in word_to_guess:
        if letter == letter_picked:
            hidden_word_list[counter] = letter_picked
        counter += 1
    return ''.join(hidden_word_list)


# This is the main loop which loops whilst the user has lives or whilse the word
# to guess is not fully alphabetical e.g. "_e__o" meaning that there are still letters to be guessed
while wrong_counter <= max_lives and not hidden_word.isalpha():
    guessed_letter = input("Please guess a letter...")   # user guesses a letter
    if guessed_letter in hidden_word or guessed_letter in incorrect_letters: # if guessed letter is in the hidden_word or incorrect_letters list then it has already been guessed
        print("You have already guessed this letter you fool...")
        wrong_counter += 1   # they loose a life for this
    elif guessed_letter in word_to_guess:  # if the guessed letter is in the word to guess
        print("That was correct!")
        hidden_word = reveal_letter(guessed_letter, word_to_guess, hidden_word) # call the function to reveal the letter in the word
        print(hidden_word)  # print the word e.g. "_e_ll_"
    else:
        wrong_counter += 1  # otherwise, they just guessed a letter that was not in the word to guess and not already guessed before
        incorrect_letters.append(guessed_letter)
        print("Incorrect!")