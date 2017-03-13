# coding=utf-8
# A. Pupils Redistribution

n=int(raw_input())
A=map(int,raw_input().split())
B=map(int,raw_input().split())

Adict={1:0,2:0,3:0,4:0,5:0}
Bdict={1:0,2:0,3:0,4:0,5:0}

for i in range(n):
	Adict[A[i]]+=1
	Bdict[B[i]]+=1

def func():
	ans=0
	for i in range(1,6):
		t=Adict[i]-Bdict[i]
		if t%2==1:
			print -1
			return
		else:
			if t>0:
				ans+=t
	print ans/2
	return
func()

'''
input
4
5 4 4 4
5 5 4 5
output
1

input
6
1 1 1 1 1 1
5 5 5 5 5 5
output
3

input
1
5
3
output
-1

input
9
3 2 5 5 2 3 3 3 2
4 1 4 1 1 2 4 4 1
output
4

题意相当于：通过交换上下行的数字，让上下两行中每个数字出现的次数相同。输入最少交换的次数。

很容易知道，如果一个数在上下两行出现的次数之和是奇数，那么一定不能达到要求，输出-1，
当某一个上下两行出现次数的差为x，那么需要从上往下挪动x/2次，
若差为-x次，则从下往上挪动x/2次，考虑交换，则交换x/2次。
计算从上往下挪动的次数（从下往上也是相同的次数，只是正负不同），即为交换次数。
'''