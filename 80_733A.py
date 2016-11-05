# coding=utf-8
# 733A. Grasshopper And the String

vovels=['A','E','I','O','U','Y']
inputs='S'+raw_input()
n=len(inputs)
temp=0
ma=0
for i in range(n):
	if inputs[i] in vovels:
		if (i-temp)>ma:
			ma=i-temp
		temp=i
if (n-temp)>ma:
	ma=n-temp
print ma

"""
input
ABABBBACFEYUKOTT
output
4
input
AAA
output
1

题目：
蟋蟀跳字符串， 只能跳'A', 'E', 'I', 'O', 'U' and 'Y'，问跳跃能力。

分析：
1.是从字符外开始跳的，所以人工增加第一个字符'S'。
2.目的并不是最后一个字符，最后一步很有可能是答案。所以遍历完需要考虑这个。
"""