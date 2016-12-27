# coding=utf-8
# B. Santa Claus and Keyboard Check 圣诞老人和键盘检查

s=raw_input()
t=raw_input()

def function():
	r={}
	ans=[]
	c=0
	for i in range(len(s)):
		if s[i] in r:
			if r[s[i]]!=t[i]:
				print -1
				return
		elif t[i] in r:
			if r[t[i]]!=s[i]:
				print -1
				return
		else:
			if s[i]==t[i]:
				r[s[i]]=t[i]
			else:
				r[s[i]]=t[i]
				r[t[i]]=s[i]
				ans.append([s[i],t[i]])
				c+=1
	if c==0:
		print 0
	else:
		print c
		for item in ans:
			print item[0],item[1]

function()

"""
input
helloworld
ehoolwlroz
output
3
h e
l o
d z

input
hastalavistababy
hastalavistababy
output
0

input
merrychristmas
christmasmerry
output
-1

http://codeforces.com/problemset/problem/748/B
圣诞老人检查拆卸键盘后重装，有些按键所在位置错了。
给出他想输出的字符串和实际输出的字符串，指出哪些按键需要交换。
没有输出0，不可能输出-1

设置一个字典存需要交换的，事实上这个字典最大长度26
例如h和e交换，就存h:e e:h
如果出现矛盾，就直接输出-1
"""