# coding:utf-8
# 814A

def judge():
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    if k > 1:
        return 'Yes'
    else:
        if a[0] == 0:
            a[0] = b[0]
        for i in range(1, n):
            if a[i] == 0:
                a[i] = b[0]
            if a[i] <= a[i - 1]:
                return 'Yes'
        return 'No'


print judge()

'''
Examples
Input
4 2
11 0 0 14
5 4
Output
Yes
Input
6 1
2 3 0 8 9 10
5
Output
No
Input
4 1
8 94 0 4
89
Output
Yes
Input
7 7
0 0 0 0 0 0 0
1 2 3 4 5 6 7
Output
Yes


显然，当不止一个 0 时（0 个数与 k 相等），肯定 Yes，因为b中这些数可以按非递增序列排。
只有一个 0 时替换为 b 中的数，看看是否递增。
'''