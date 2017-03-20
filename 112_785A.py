# coding=utf-8
# 785A. Anton and Polyhedrons 安东和多面体

n = int(raw_input())
re = {'Tetrahedron': 4, 'Cube': 6, 'Octahedron': 8, 'Dodecahedron': 12, 'Icosahedron': 20}
ans = 0
for i in range(n):
    polyhedron = raw_input()
    ans += re[polyhedron]
print ans

"""
input
4
Icosahedron
Cube
Tetrahedron
Dodecahedron
output
42

input
3
Dodecahedron
Octahedron
Octahedron
output
28

给出多面体数量和名称，求一共多少个面。
"""