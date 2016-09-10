n=int(raw_input())
row=int((2*n)**0.5)
temp=(row+1)*row/2

if temp==n:
	print row
elif temp<n:
	print n-temp
else:
	print row-(temp-n)