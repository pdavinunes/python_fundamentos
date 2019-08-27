sal = float(input())

if sal <= 2000.00:
	print('Isento')
elif sal <= 3000.00:
	imp = (sal - 2000.00) * 0.08
	print('R$ {:.2f}'.format(imp)) 
elif sal <= 4500.00:
	imp1 = (1000.00) * 0.08
	imp2 = (sal - 3000.00) * 0.18
	print('R$ {:.2f}'.format(imp1+imp2))  
else:
	imp1 = (1000.00) * 0.08
	imp2 = (1500.00) * 0.18
	imp3 = (sal - 4500.00) * 0.28
	print('R$ {:.2f}'.format(imp1+imp2+imp3)) 