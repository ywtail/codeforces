# coding=utf-8
# 769A. Year of University Entrance

n=int(raw_input())
A=map(int,raw_input().split())

if n==1:
	print A[0]
else:
	print (max(A)+min(A))/2

'''
input
3
2014 2016 2015
output
2015

input
1
2050
output
2050

题目地址：http://codeforces.com/contest/769/problem/A
题目相当于：找出一堆年份的中间年份。
分析：难点在读懂题意。
题中不仅限制了n为奇数，n最大为5，还假定了答案一定存在，实在没什么难度。
'''