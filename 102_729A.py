# coding=utf-8
# 729A. Interview with Oleg

import re
n=int(raw_input())
s=raw_input()
print re.subn('o(go)+','***',s)[0]

"""
input
7
aogogob
output
a***b

input
13
ogogmgogogogo
output
***gmg***

input
9
ogoogoogo
output
*********

http://codeforces.com/problemset/problem/729/A
找ogogogo
"""