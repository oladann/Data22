
# This is a dictionary of a bunch of key-value pairs of
# "scrabble" numbers which each correspond to a set value

SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

# new function made called scrabble_score
def scrabble_score(word):
    # counter total set to 0 , Python's indexing starts at 0
    total = 0
    # initiate "for loop", for each letter value stored in the dictionary
    # based on its respective key, add up the corresponding value each time for each
    # letter, so i.e for "letter", we should return the value: 1+1+1+1+1+1= 6
    for letter in word:
        total += SCORES[letter]
    return total
# In this variable "WORD to type in the word in which you wanna
# find its total scrabble value and the function is outputted in console using "print"
WORD = scrabble_score("letter")
print(WORD)
