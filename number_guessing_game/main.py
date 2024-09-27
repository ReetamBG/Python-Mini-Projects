import random 

print('Enter the range of numbers')

while(1):
	try:
		range = int(input('Low : ')), int(input('High : '))
		break
	except:
		print('Enter a valid number')

n = random.randint(range[0], range[1])
lives = 3

while(lives):
	print('*' * 20)
	print(f'Lives Remaining : {lives}')
	
	guess = input('Guess the number (x to exit): ')

	if guess.lower() == 'x':
		print('*' * 20)
		print('Session ended by player')
		break

	# If no input is given start over the loop else typecast input to int
	# No input or non numeric inputs will give error when typecasting to int
	try:
		guess = int(guess)
	except:
		print('*' * 20)
		print('Please enter a number')
		continue

	if guess == n:
		print('*' * 20)
		print('Yayy you won!!')
		break;
	lives -= 1;

if lives == 0:
	print('*' * 20)
	print(f'Lives ended you lost\nThe correct number was {n}')
