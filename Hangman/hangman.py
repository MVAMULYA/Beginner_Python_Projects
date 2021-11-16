# !usr/bin/env Python3

import random

f = open("word_list.txt", "r")

list_of_words = f.read().split()
word = random.choice(list_of_words)
revealed_word = ['_' for i in word]
wrong_guess = 10
guess = 0
while guess < wrong_guess:
    letter = input("Enter alphabet: ")
    if letter in word:
        indexes = [i for i, l in enumerate(word) if letter == l]
        for index in indexes:
            revealed_word[index] = letter
        print(''.join(revealed_word))
    else:
        guess += 1
        print(f"Remaing Guesses : {wrong_guess-guess}")
    
    if "_" not in revealed_word:
        break
if "_" in revealed_word:
    print(f"You loose. The word is {word}")