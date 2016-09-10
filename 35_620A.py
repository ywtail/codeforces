x1,y1=map(int,raw_input().split())
x2,y2=map(int,raw_input().split())

x=abs(x1-x2)
y=abs(y1-y2)

print abs(x-y)+min(x,y)
