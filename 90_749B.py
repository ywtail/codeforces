#coding=utf-8
#749B. Parallelogram is Back

x1,y1=map(int,raw_input().split())
x2,y2=map(int,raw_input().split())
x3,y3=map(int,raw_input().split())

ans=[(x3-(x1-x2),y3-(y1-y2)),(x3+(x1-x2),y3+(y1-y2)),(x2-(x1-x3),y2-(y1-y3)),(x2+(x1-x3),y2+(y1-y3)),(x1-(x2-x3),y1-(y2-y3)),(x1+(x2-x3),y1+(y2-y3))]
ans=list(set(ans))
print 3
for (x,y) in ans:
	print x,y

"""
0 0
1 0
0 1

3
1 -1
-1 1
1 1

题目：http://codeforces.com/problemset/problem/749/B
input:坐标系中三个点，
output:要构成平行四边形，第四个点有几种可能，分别是什么

第四个点肯定有3种情况
"""