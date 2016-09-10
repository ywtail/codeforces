n=int(raw_input())

bitn=bin(n)
reversebitn=bitn[::-1]

kintegers=[]

for i in xrange(0,len(reversebitn)):
	if reversebitn[i]=="1":
		kintegers.append(i+1)

for x in kintegers[::-1]:
	print x,
