# coding=utf-8
# 780A. Andryusha and Socks

n=int(raw_input())
x=raw_input().split()
remenber={}
ans=0
t=0
for i in range(n*2):
	if x[i] not in remenber:
		remenber[x[i]]=1
		t+=1
	else:
		t-=1
	if t>ans:
		ans=t
print ans

'''
input
1
1 1
output
1

input
3
2 1 1 3 2 3
output
2

相当于：关注输入中第二行的序列，如果整数之前没出现过则放桌上，出现过则拿走，
问桌上最多放了几个整数。

这一题不定义remenber={}(单词正确拼写remember)也能做，可以直接
if x[i] in x[:i]
但是由于in搜索在字典中比列表快，所以依然定义这个dict。
'''