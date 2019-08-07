import random

nomes = ['ABELHA','CHAVE','CORDA','MACACO','CELULAR','APOLLO']

nivel = int(input('Escolha o nivel do jogo -> [1 - Facil] [2 - Medio] [3 - Dificil] '))

chances = 0 

if nivel == 1:
	print('Você terá 9 chances!')
	chances = 9
elif nivel == 2:
	print('Você terá 6 chances!')
	chances = 6
else:
	print('Você terá 3 chances!')
	chances = 3

palavra_secreta = nomes[random.randint(0,len(nomes) - 1)];
letras_chutadas = []
nome = []

for x in range(0,len(palavra_secreta)):
	nome.append('_')

def draw_nome(letra):
	for x in range(0,len(palavra_secreta)):
		if letra.upper() == palavra_secreta[x]:
			letras_chutadas.append(letra)
			nome[x] = letra.upper()
		else:
			chances -= 1
			letras_chutadas.append(letra)

def win():
	if '_' in nome:
		return False
	else:
		return True

while not win() and chances >= 1:
	print('Chances restantes ->',chances)
	print(nome)
	letra = input('Digite uma letra  -> ')
	if letra in letras_chutadas:
		print('Letra já chutada')
	else:
		draw_nome(letra)