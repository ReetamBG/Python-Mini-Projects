import random 

words = []
print('Enter the words')

while True:
	word = input(f'Enter word {len(words)} (Enter blank to exit) : ')
	if word == '':
		break
	words.append(word)

random_word = random.choice(words)
random_word_list = [char for char in random_word]    # converting to list for easier operations
guesses = 5

correct_guesses = []    # to keep track of the correct characters guessed
final_word = ['_' for char in random_word]    # to keep track of the score

print(f'Guess the word\n{' '.join(final_word)}')

while guesses:
	print('*' * 20)
	guess = input('Guess a character (Enter blank to exit) : ')

	if guess == '':
		print('*' * 20)
		print('Session ended by player')
		break
	if not guess.isalpha() or len(guess)!=1:
		print('Please enter a single alphabet')
		continue
	
	if guess in random_word:    # guess.isin(word) is for pandas for python we have in keyword
		correct_guesses.append(guess)
		print('*' * 20)
		for i in range(len(random_word_list)):
			char = random_word_list[i]
			if char in correct_guesses:
				final_word[i] = char

		print(f'Weee\n{' '.join(final_word)}')
	
	else:
		print(f'No letter {guess} in the word')
		print(f'Guesses Remaining : {guesses}')
		guesses -= 1;

	if final_word == random_word_list:
		print('*' * 20)
		print(f'Yayy!! You Won\nThe correct word was {random_word}')
		break;

if guesses == 0:
	print('*' * 20)
	print(f'Guesses ended you lost\nThe correct word was {random_word}')
