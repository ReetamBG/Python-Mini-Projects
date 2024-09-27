import random 

print('Enter the range of numbers')
range = int(input('Low : ')), int(input('High : '))

n = random.randint(range[0], range[1])
lives = 3

while(lives):
	print('*' * 10)
	print(f'Lives Remaining : {lives}')
	guess = int(input('Guess the number : '))
	if guess == n:
		print('Yayy you won!!')
		break;
	lives -= 1;

if lives == 0:
	print(f'Lives ended you lost\nThe correct number was {n}')
