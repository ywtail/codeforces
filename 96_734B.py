# coding=utf-8
#734B. Anton and Digits 32和256

k2,k3,k5,k6=map(int,raw_input().split())
t=min(k2,k5,k6)
print 256*t+32*min(k2-t,k3)

"""
input
5 1 3 4
output
800

input
1 1 1 1
output
256

http://codeforces.com/problemset/problem/734/B
There are k2 digits 2, k3 digits 3, k5 digits 5 and k6 digits 6.
用这些数组成32和256，求组成的这些数的和（最大）。

显然，先组成最多的256，再组成32.
"""