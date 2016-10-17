#coding=utf-8

n=int(raw_input())
inputs=[]
row=[0 for i in range(n)]
col=[0 for i in range(n)]
num=0

for i in range(n):
	inputs.append(raw_input())

for i in range(n):
	for j in range(n):
		if inputs[i][j]=='C':
			row[i]+=1
			col[j]+=1

for i in range(n):
	if row[i]>=2:
		num+=row[i]*(row[i]-1)/2
	if col[i]>=2:
		num+=col[i]*(col[i]-1)/2

print num