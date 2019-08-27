a , b = 0, 1, 

n = int(input())

print('%d %d ' %(a, b), end = '')
for x in range(2,n-1):
 	print('%d ' %(a+b), end = '')
 	tmp = b
 	b = b + a
 	a = tmp 

print('%d' %(a+b))
