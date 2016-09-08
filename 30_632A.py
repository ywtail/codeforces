n,p=map(int,raw_input().split())
inputs=[]
for i in xrange(0,n):
	inputs.append(raw_input())

temp=0.5
total=0.5

if n>1:
	for key in inputs[n-2::-1]:
		if key=="half":
			temp=temp*2
			total+=temp
		else:
			temp=temp*2+0.5
			total+=temp

print int(p*total)
