n,m=map(int,raw_input().split())
matrix=""

for i in xrange(0,n):
	matrix+=raw_input()

def repla(matrix,s):
	return len(matrix)-len(matrix.replace(s,''))

if repla(matrix,'C')>0 or repla(matrix,'M')>0 or repla(matrix,'Y')>0:
	print "#Color"
else:
	print "#Black&White"
	