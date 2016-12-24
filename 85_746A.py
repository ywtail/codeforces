#coding=utf-8
#746A. Compote 蜜饯

a=int(raw_input())
b=int(raw_input())
c=int(raw_input())

print min(min(c/2,b)/2,a)*7

"""
2
5
7

7

题目：http://codeforces.com/problemset/problem/746/A
a:b:c=1:2:4，按这个比例做compote，问一共需要多少个a b c
"""