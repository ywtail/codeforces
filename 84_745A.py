# coding=utf-8
# 745A. Hongcow Learns the Cyclic Shift

s=raw_input()
n=len(s)
temp=[]
ans=0
if len(set(s))==1:
	print 1
else:
	for i in range(1,n+1):
		if s[(n-i):]+s[:(n-i)] not in temp:
			temp.append(s[(n-i):]+s[:(n-i)])
			ans+=1
	print ans
		
"""
http://codeforces.com/contest/745/problem/A
将最后一个字母放到最前面，看一共能形成多少个不同的字符串。
例如："abcd", "dabc", "cdab", and "bcda".

abab，2种
ababab,2种
不好用找规律来解决，而题中说明字符串长度不超过50，所以可以直接枚举。
"""