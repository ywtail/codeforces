#coding=utf-8

a,b=map(int,raw_input().split())
outputs=[b]
num=1
while b>a:
	if b%2==0:
		b=b/2
		outputs.append(b)
		num+=1
	else:
		if (b-1)%10==0:
			b=(b-1)/10
			outputs.append(b)
			num+=1
		else:
			break
if a==b:
	print "YES"
	print num
	for x in outputs[::-1]:
		print x,
else:
	print "NO"
