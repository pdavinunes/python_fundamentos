e = int(input())
d = int(input())

if d - e <= 3:
	print('Muito bem! Apresenta antes do Natal!')
elif d - e < 0:
	print('Eu odeio a professora!')
else:
	print('Parece o trabalho do meu filho!')
	if d + e < 3:
		print('TCC Apresentado!')
	else:
		print('Fail! Entao eh nataaaaal!')