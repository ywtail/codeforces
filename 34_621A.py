n=raw_input()
integers=map(int,raw_input().split())
odds=[]
for integer in integers:
	if integer%2==1:
		odds.append(integer)

sumall=sum(integers)

if sumall%2==0:
	print sumall
else:
	print sumall-sorted(odds)[0]
