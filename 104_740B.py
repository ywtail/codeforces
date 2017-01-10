# coding=utf-8
# 740B. Alyona and flowers

n,m=map(int,raw_input().split())
a=map(int,raw_input().split())
ans=0
for i in range(m):
	l,r=map(int,raw_input().split())
	temp=sum(a[l-1:r])
	if temp>0:
		ans+=temp
print ans

"""
input
5 4
1 -2 1 3 -4
1 2
4 5
3 4
1 4
output
7

input
4 3
1 2 3 4
1 3
2 4
1 1
output
16

input
2 2
-1 -2
1 1
1 2
output
0

http://codeforces.com/problemset/problem/740/B
For example, consider the case when the mother has 5 flowers, and their moods are equal to 1,  - 2, 1, 3,  - 4. Suppose the mother suggested subarrays (1,  - 2), (3,  - 4), (1, 3), (1,  - 2, 1, 3). Then if the girl chooses the third and the fourth subarrays then:
the first flower adds 1·1 = 1 to the girl's happiness, because he is in one of chosen subarrays,
the second flower adds ( - 2)·1 =  - 2, because he is in one of chosen subarrays,
the third flower adds 1·2 = 2, because he is in two of chosen subarrays,
the fourth flower adds 3·2 = 6, because he is in two of chosen subarrays,
the fifth flower adds ( - 4)·0 = 0, because he is in no chosen subarrays.
Thus, in total 1 + ( - 2) + 2 + 6 + 0 = 7 is added to the girl's happiness. 

虽然题目说的如此复杂，但是，只要每一个子数组贡献的值为正，就可以选入。
不需要先统计每个数出现多少次。
"""