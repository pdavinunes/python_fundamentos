import random

def gera():
	mini = int(input('Defina o numero minimo -> '))
	maxi = int(input('Defina o numero maximo -> '))
	return random.randint(mini, maxi)

print('Seu numero é:', gera())

while input('Novo numero? [y/n] -> ') == 'y':
	print('Seu numero é', gera())