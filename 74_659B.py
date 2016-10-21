#coding=utf-8
from operator import itemgetter
n,m=map(int,raw_input().split())
inputs=[]
for i in range(n):
	a,b,c=raw_input().split()
	inputs.append([a,int(b),int(c)])

sort_inputs=sorted(inputs,key=itemgetter(1,2),reverse=True)

outputs=[]
book=[0 for i in range(m)]
p=0
while p<n-1:
	temp=sort_inputs[p][1]
	if book[temp-1]==0:
		book[temp-1]=1
		if p<n-2 and book[sort_inputs[p+2][1]-1]==1 and sort_inputs[p+1][2]==sort_inputs[p+2][2]:
			outputs.append('?')
		else:
			outputs.append(sort_inputs[p][0]+' '+sort_inputs[p+1][0])
		p+=2
	else:
		p+=1

for x in outputs[::-1]:
	print x

"""
input
5 2
Ivanov 1 763
Andreev 2 800
Petrov 1 595
Sidorov 1 790
Semenov 2 503
output
Sidorov Ivanov
Andreev Semenov

input
5 2
Ivanov 1 800
Andreev 2 763
Petrov 1 800
Sidorov 1 800
Semenov 2 503
output
?
Andreev Semenov
"""