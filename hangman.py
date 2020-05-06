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
			|	   \\|/
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
	print("\n You Are On Level " , level)
	print("\n")
	draw(attempts_left)
	while not correct and attempts_left > 0:
		print(complete)
		print("\n")
		attempt = input("Please guess a letter or word: " ).lower()
		if len(attempt) == 1 and attempt.isalpha():
			if attempt in letters_guess:
				print("You've already guessed the letter: " ,attempt)
			elif attempt not in target_word:
				attempts_left -= 1
				draw(attempts_left)
				print("The letter [",attempt,"] is not in the word. Try again")
				letters_guess.append(attempt)
			else:
				draw(attempts_left)
				print("You guessed a correct letter")
				letters_guess.append(attempt) 
				convert_word = list(target_word)
				display = list(complete)
				addToWord(convert_word, attempt, display)
				complete = ''.join(display)
				if complete == target_word:
					correct = True	
		elif len(attempt) == len(target_word) and attempt.isalpha():
			if attempt in words_guess:
				print("You've already guessed the word: " ,attempt)
			elif attempt != target_word: 
				attempts_left -= 1
				draw(attempts_left)
				print(attempt," is not the correct word. Try again")
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
		return 1
	else:
		print("Sorry the guy you were supposed to save has been hanged. \nThe word was [" ,target_word ,"] \nThe HANGMAN has won. \nGame Over.")
		return 0


def main():
	use_word = what_word_to_use()
	level = 1	
	game("hello", level)
	while level < 10:
		play_on = input("Move on the next level? Yes/No: ")
		if play_on[0] == "y" or play_on[0] == "Y": 
			use_word = what_word_to_use()
			level = level + 1
			game(use_word, level)
		else:
			break




if __name__ == '__main__':
	main()

