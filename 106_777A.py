# coding=utf-8
# 777A. Shell Game

n=int(raw_input())
x=int(raw_input())
temp=[[0,1,2],[1,0,2],[1,2,0],[2,1,0],[2,0,1],[0,2,1]]
print temp[n%6][x]

"""
input
4
2
output
1

input
1
1
output
0

找规律，每6个一循环
"""