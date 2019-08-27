row = int(input())

imp = []
imp.extend(range(1,row*2,2))

col = imp[row-1] + 2
print(row,col)

print(int(col/row)+1)

mat = []

for x in range(0,row):
	for y in range(0,col):
		mat[x][y] = 0

print(mat)