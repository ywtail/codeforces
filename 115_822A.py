 # coding:utf-8
 # 822A. I'm bored with life
a, b = map(int, raw_input().split())
t = min(a, b)
ans = 1
for i in range(2, t + 1):
    ans *= i
print ans

'''
Example
input
4 3
output
6

求a、b阶乘的最大公约数。
显然答案是 min(a,b)!，题中指出 min(a,b)<=12，所以不用考虑整型溢出问题。
'''