# coding=utf-8
# 779B. Weird Rounding

n,k=raw_input().split()
k=int(k)
length=len(n)

if n=='0':
	print 0
else:
	t=n.count('0')
	if t<k:
		print length-1
	else:
		ans=0
		count0=0
		i=length-1
		while count0<k:
			if n[i]=='0':
				count0+=1
			else:
				ans+=1
			i-=1
		print ans

'''
input
30020 3
output
1

input
100 9
output
2

input
10203049 2
output
3

题目地址：http://codeforces.com/problemset/problem/779/B

题目相当于：
给出n和k，要求通过移除n的某一位，使n能够被10^k整除。输出移除的位数。

因为题目假设答案存在，所以如果n不是0则至少包含一个0，所以第12、13行可以那么写，而不必考虑不能整除的情况。
需要注意的是，可以将整数n当字符串来进行处理，但是不要忘记将k转为int，不然第12行条件判断始终为True。
'''