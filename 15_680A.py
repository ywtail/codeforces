from collections import Counter

numbers=map(int,raw_input().split())
total=sum(numbers)

numdic=dict(Counter(numbers))
numlist=sorted(numdic.iteritems(),key=lambda d:d[0])

def func(x):
	return x[1]>1

number=filter(func,numlist)

s=[]
if len(number)==0:
	print total
else:
	for n in number:
		if n[1]<4:
			s.append(n[0]*n[1])
		else:
			s.append(n[0]*3)
	print total-max(s)
