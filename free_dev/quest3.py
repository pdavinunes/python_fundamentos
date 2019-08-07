import random

dict = {'Nomes' : [], 'Adjetivos' : [], 'Locais': [], 'Comidas': [], 'Corpo': []}

for x in range(0,4):

	dict['Nomes'].append(input('Digite um nome proprio -> '))
	dict['Corpo'].append(input('Digite uma parte do corpo -> '))
	if x <= 2:
		dict['Locais'].append(input('Digite um local com seu pronome -> ')) 
		dict['Comidas'].append(input('Digite uma comida -> '))	
	if x <= 1:
		dict['Adjetivos'].append(input('Digite um adjetivo -> ')) 
	

random.shuffle(dict['Nomes'])
random.shuffle(dict['Locais'])
random.shuffle(dict['Adjetivos'])
random.shuffle(dict['Comidas'])
random.shuffle(dict['Corpo'])

print('%s é uma pessoa muito %s e estava %s e decidiu comer um(a) %s.' 
%(dict['Nomes'][0], dict['Adjetivos'][0],dict['Locais'][0], dict['Comidas'][0])) 

print('%s pediu um pouco, então %s jogou seu(sua) %s na %s de %s.' 
%(dict['Nomes'][1], dict['Nomes'][0], dict['Corpo'][0], dict['Corpo'][1], dict['Nomes'][1]))

print('Mais tarde %s estava %s, então %s comeu %s e esfregou seu(sua) %s no(a) %s de %s.' 
%(dict['Nomes'][2],dict['Locais'][1],dict['Nomes'][2],dict['Comidas'][1],dict['Corpo'][2],dict['Corpo'][1],dict['Nomes'][0]))

print('%s é um pouco %s, foi até %s lambeu o(a) %s de %s, depois comeu %s sobre o(a) %s de %s'
%(dict['Nomes'][3],dict['Adjetivos'][1],dict['Locais'][2],dict['Corpo'][2],dict['Nomes'][0],dict['Comidas'][2],dict['Corpo'][3],dict['Nomes'][1]))