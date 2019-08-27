def verificaTri(a,b,c):
	return a + b > c

inp = input().split()
a, b, c = float(inp[0]), float(inp[1]), float(inp[2])

if verificaTri(a,b,c) and verificaTri(c,b,a) and verificaTri(a,c,b):
	print('Perimetro = {:.1f}'.format(a+b+c) )
else:
	print('Area = {:.1f}'.format(float((a+b)*c)/2.0))