a,ta=map(int,raw_input().split())
b,tb=map(int,raw_input().split())
h,m=map(int,raw_input().split(":"))
time=(h-5)*60+m

start=[time-tb,0][time-tb<0]
end=min(time+ta,1140)

stemp=start/b+1 if time-tb>=0 else start/b
etemp=end/b if end%b!=0 else end/b-1

print etemp-stemp+1