matriz = {
	'a':'abcdefghijklmnopqrstuvwxyz',
	'b':'bcdefghijklmnopqrstuvwxyza',
	'c':'cdefghijklmnopqrstuvwxyzab',
	'd':'defghijklmnopqrstuvwxyzabc',
	'e':'efghijklmnopqrstuvwxyzabcd',
	'f':'fghijklmnopqrstuvwxyzabcde',
	'g':'ghijklmnopqrstuvwxyzabcdef',
	'h':'hijklmnopqrstuvwxyzabcdefg',
	'i':'ijklmnopqrstuvwxyzabcdefgh',
	'j':'jklmnopqrstuvwxyzabcdefghi',
	'k':'klmnopqrstuvwxyzabcdefghij',
	'l':'lmnopqrstuvwxyzabcdefghijk',
	'm':'mnopqrstuvwxyzabcdefghijkl',
	'n':'nopqrstuvwxyzabcdefghijklm',
	'o':'opqrstuvwxyzabcdefghijklmn',
	'p':'pqrstuvwxyzabcdefghijklmno',
	'q':'qrstuvwxyzabcdefghijklmnop',
	'r':'rstuvwxyzabcdefghijklmnopq',
	's':'stuvwxyzabcdefghijklmnopqr',
	't':'tuvwxyzabcdefghijklmnopqrs',
	'u':'uvwxyzabcdefghijklmnopqrst',
	'v':'vwxyzabcdefghijklmnopqrstu',
	'w':'wxyzabcdefghijklmnopqrstuv',
	'x':'xyzabcdefghijklmnopqrstuvw',
	'y':'yzabcdefghijklmnopqrstuvwx',
	'z':'zabcdefghijklmnopqrstuvwxy'
	}

msg_total = input('Digite a mensagem -> ')

msg_total = msg_total.split()

key = msg_total[0]
msg = msg_total[1]

while len(key) < len(msg):
	key *= 2

key = key[:len(msg)]

msg_crif = ''

for i in range(0,len(key)):
	index1 = matriz['a'].index(key[i])

	msg_crif += matriz[msg[i]][index1]

print(msg_crif)