n=raw_input()
alist=map(int,raw_input().split())
blist=map(int,raw_input().split())

a=0
b=0

for x in alist:
	a=a|x

for y in blist:
	b=b|y

print a+b
	
