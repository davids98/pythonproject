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

def addToWord(word,letter,display):
	instance = []
	for x in range(len(word)):
		if letter == word[x]:
			instance.append(x)
	for j in range(len(instance)):
		display[instance[j]] = word[instance[j]]			

def game(target_word, level):
	complete = "_"  * len(target_word)
	correct = False;
	letters_guess = []
	words_guess = []
	attempts_left = 6
	if level == 1:
		print("\n H A N G M A N \n")
		input("Press Enter To Begin ..." )
	print("You Are On Level " , level)
	print("\n")
	
	while not correct and attempts_left > 0:
		print(complete)
		print("\n")
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
				convert_word = list(target_word)
				display = list(complete)
				addToWord(convert_word, attempt, display)
				complete = ''.join(display)
				if "_" not in complete:
					correct == True	
		elif len(attempt) == len(target_word) and attempt.isalpha():
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
	while input("Move on the next level Y/N: ").lower == "y"  and level < 10:
		use_word = what_word_to_use()
		level = level + 1
		game(use_word, level)
	

main()
