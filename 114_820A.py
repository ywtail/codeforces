# coding:utf-8
# 820A. Mister B and Book Reading
c, v0, v1, a, l = map(int, raw_input().split())
t = 0
while c > 0:
    v = min(v1, v0 + t * a)
    if c <= v:
        t += 1
        break
    c = c - v + l
    t += 1
print t

'''
Examples
input
1 1 1 8
output
2
input
4 2 2 6
output
3
input
3 7 4 6
output
1

输入分别是：书的长度，初始读取速度，最大读取速度，读取速度的加速度和重新读取的页面数量。
求几天读完。
'''