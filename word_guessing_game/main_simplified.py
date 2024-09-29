import random 

words = []
print('Enter the words')

while True:
	word = input(f'Enter word {len(words)} (Enter blank to exit) : ')
	if word == '':
		break
	words.append(word)

random_word = random.choice(words)
correct_guesses = ''
guesses = 5


print(f'Guess the word\n{' '.join([' _ ' for char in random_word])}')

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
	
	for char in correct_guesses:
		if guess == char:
			correct_guesses = correct_guesses + guess
	
	if guess not in random_word:
		print(f'No letter {guess} in the word')

	correctly_guesses = True
	for char in random_word:
		if char in correct_guesses:
			print(char, end=' ')
			correct_guesses = correct_guesses + guess
		else:
			print('_', end=' ' )
			correctly_guessed = False
	
	if correctly_guessed == True:
		print('*' * 20)
		print(f'Yayy you win!!\nThe correct word is {random_word}')
	

if guesses == 0:
	print('*' * 20)
	print(f'Guesses ended you lost\nThe correct word was {random_word}')
