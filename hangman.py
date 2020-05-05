import random # import random lib
from word_bank import words_to_choose # import the wordbank 



def draw(attempt):
	hanglist =[
		"""     \t\t\t-------------
			|
			|
			|
			|
			|
			|
			|
			|
		       / \\ 
		""",

		"""     \t\t\t-------------
			|	    |
			|	    O
			|
			|
			|
			|
			|
			|
		       / \\ """,
		"""     \t\t\t-------------
			|	    |
			|	    O
			|	    |
			|	    |      
			|
			|
			|
			|
		       / \\ """,

		"""     \t\t\t-------------
			|	    |
			|	    O
			|	    |
			|	    |      
			|	   /
			|
			|
			|
		       / \\ """,
		"""    \t\t\t -------------
			|	    |
			|	    O
			|	    |
			|	    |      
			|	   / \\
			|
			|
			|
		       / \\ """,
	
		"""     \t\t\t-------------
			|	    |
			|	    O
			|	    |/
			|	    |      
			|	   / \\
			|
			|
			|
		       / \\ """,
		"""     \t\t\t-------------
			|	    |
			|	    O
			|	   \\ |/
			|	    |      
			|	   / \\
			|
			|
			|
		       / \\ """
	]
	print(hanglist[6 - attempt])

def what_word_to_use():
	target_word = random.choice(words_to_choose)
	return target_word.lower()

def game(target_word, level):
	complete = "_"  * len(target_word)
	correct = False;
	letters_guess = []
	words_guess = []
	attempts_left = 5
	if level == 1:
		print("\n H A N G M A N \n")
		input("Press Enter To Begin ..." )
	print("You Are On Level " , level)
	print("\n")
	print(complete)
	print("\n")
	while not correct and attempts_left > 0:
		attempt = input("Please guess a letter or word: " ).lower()
		if len(attempt) == 1 and attempt.isalpha():
			if attempt in letters_guess:
				print("You've already guessed the letter: " ,attempt)
			elif attempt not in target_word:
				draw(attempts_left)
				print("The letter [",attempt,"] is not in the word. Try again")
				attempts_left -= 1
				letters_guess.append(attempt)
			else:
				draw(attempts_left)
				print("You guessed a correct letter")
				letters_guess.append(attempt) 
				convert_word_to_list = list(target_word)
				letters = [x for x, letter in enumerate(convert_word_to_list) if letter == attempt]
				for number in letters:
					convert_word_to_list[number] = attempt
				complete = "".join(convert_word_to_list)
				if "_" not in complete:
					correct == True	
		elif len(attempt) == len(word) and attempt.isalpha():
			if attempt in words_guess:
				print("You've already guessed the word: " ,attempt)
			elif attempt != target_word: 
				draw(attempts_left)
				print(attempt," is not the correct word. Try again")
				attempts_left -= 1
				words_guess.append(attempt)
			else: 
				correct = True
				complete = target_word
		elif len(attempt) > 1 and attempt.isalpha():
			print("Guess does not have correct amount of letters. Try again." )
		else: 
			print("Not a valid input. Please try again" )

	if correct:
		print("You win this level!")
	else:
		print("Sorry you killed the man by using all your attempts. The word was " ,target_word ," Game Over.")





def main():
	use_word = what_word_to_use()
	level = 1	
	game(use_word, level)
	while input("Move on the next level Y/N: ").lower == "y"  and level < len(words_to_choose):
		use_word = what_word_to_use()
		level = level + 1
		game(use_word, level)
	

main()
