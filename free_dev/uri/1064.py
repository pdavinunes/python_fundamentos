cont = 0
tot = 0

for n in range(0,6):
	x = float(input())
	if x > 0:
		tot += x
		cont += 1

print('%d valores positivos' %(cont))
print('{:.1f}'.format(tot/cont))