import random # import random lib
from word_bank import words_to_choose # import the wordbank 

def what_word_to_use():
	target_word = random.choice(words_to_choose)
	return target_word.lower()

def game(target_word, level):
	complete = "_"  * len(target_word)
	correct = False;
	letters_guess = []
	words_guess = []
	attempts_left = 6
	if level == 0:
	print("Hangman is about to begin! \n")
	print("Level ")
	print(str(level))
	print("\n")
	print(complete)
	print("\n")
	while not corrrect and attempts_left > 0:
		attempt = input("Please guess a letter or word: " ).lower()
		if len(attempt) == 1 and attempt.isalpha():

		elif len(attempt) == len(word) and attempt.isalpha():

		elif len(attempt) > 1 and attempt.isalpha():

		else: 
			print("Not a valid input. Please try again" )
