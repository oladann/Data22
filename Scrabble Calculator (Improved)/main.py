one_letter_point = ['e', 'a', 'o', 't', 'i', 'n', 'r', 's', 'l', 'u']
two_letter_point = ['d', 'g']
three_letter_point = ['c', 'm', 'b', 'p']
four_letter_point = ['h', 'f', 'w', 'y', 'v']
five_letter_point = ['k']
eight_letter_point = ['j', 'x']
ten_letter_point = ['q', 'z']

def scrabble_word_count(word):
   score = 0
   for letter in word:
    if letter in one_letter_point:
        score += 1
    elif letter in two_letter_point:
        score += 2
    elif letter in three_letter_point:
         score += 3
    elif letter in four_letter_point:
         score += 4
    elif letter in five_letter_point:
          score += 5
    elif letter in eight_letter_point:
          score += 8
    elif letter in ten_letter_point:
          score += 10

   return score               #NOTE: the "return statement is NOT IN THE LOOP!

print(scrabble_word_count("olaoluwa ajayi"))