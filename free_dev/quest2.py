import random

def gera():
	mini = int(input('Defina o numero minimo -> '))
	maxi = int(input('Defina o numero maximo -> '))
	return random.randint(mini, maxi)

num_sec = gera()
num = int(input('Digite um numero -> '))

while num != num_sec:
	print ('Numero muito alto!' if num > num_sec else 'Numero muito baixo!')
	
	num = int(input('Digite um numero -> '))

print('Parabens voce acertou!')
print('Numero secreto ->', num_sec)