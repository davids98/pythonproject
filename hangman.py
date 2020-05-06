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

def game(target_word, level, hints):
	complete = "_"  * len(target_word)
	correct = False;
	letters_guess = []
	words_guess = []
	attempts_left = 6
	if level == 1:
		print("\n H A N G M A N \n")
		rules = input("Press Enter To Begin ...\nType in [ How ] for a HOW TO PLAY\n\n" ).lower()

		if rules == "how":	
			print("\n You Are Lawyer Tasked With Defending 10 People Set To Be Hanged ")
			print(" As You Are Making Your Case To The Hangman To Save These People You Suddenly Forget A Word On The Tip Of Your Tongue ")
			print(" You Must Remember What The Word Was Before The Hangman Kills The People You Are Set To Save \n\n")
			print(" 1) When Given The Prompt Guess A Letter Or Word ")
			print(" 2) With Each Wrong Guess The Hangman Adds A Limb. Once All Limbs Are Added The Game Is Over ")
			print(" 3) Save All 10 People To Win The Game ")
			print(" 4) You Start With One Hint That You Can Use By Typing In [ hint ] ")	
			print(" 5) Every Flawless Round Adds Another Hint For You To Use Whenever You Choose  \n")
			input("Press Enter To Begin ..." )
		
	print("\n You Are On Level " , level)
	print("\n")
	draw(attempts_left)
	while not correct and attempts_left > 0:
		print(complete)
		print("Hints: ", hints)
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
				print("You guessed a correct letter!")
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
	hints = 1	
	game("hello", level, hints)
	num_hints = hints
	while level < 10:
		play_on = input("Move on the next level? Yes/No: ")
		if play_on[0] == "y" or play_on[0] == "Y": 
			use_word = what_word_to_use()
			level = level + 1
			game(use_word, level,num_hints)
			num_hints = hints
		else:
			break




if __name__ == '__main__':
	main()

