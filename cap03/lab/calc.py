print('*'*19+' Python Calculator '+'*'*19)
print('\nSelecione o número da operação desejada:\n')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão\n')

op = int(input('Digite sua opção (1/2/3/4): '))

num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input('\nDigite o segundo número: '))

if op == 1:
	print('\n%d + %d = %d' %(num1,num2,num1+num2))
elif op == 2:
	print('\n%d - %d = %d' %(num1,num2,num1-num2))
elif op == 3:
	print('\n%d * %d = %d' %(num1,num2,num1*num2))
elif op == 4:
	print('\n%d / %d = %d' %(num1,num2,num1/num2))
else: 
	print('\nOpção inválida!')