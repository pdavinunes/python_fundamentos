inp = input().split()

num = []

num.append(float(inp[0]))
num.append(float(inp[1]))
num.append(float(inp[2]))  

num.sort(reverse = True)

a = float(num[0])
b = float(num[1])
c = float(num[2])

if a >= b + c:
	print('NAO FORMA TRIANGULO')
else:
	if a**2 == b**2 + c**2:
		print('TRIANGULO RETANGULO')
	if a**2 > b**2 + c**2:
		print('TRIANGULO OBTUSANGULO')
	if a**2 < b**2 + c**2:
		print('TRIANGULO ACUTANGULO')
	if a == b and b == c:
		print('TRIANGULO EQUILATERO')
	if (a == b and b != c) or (a == c and b != c) or (c == b and b != a):
		print('TRIANGULO ISOSCELES')