# coding=utf-8
from __future__ import division

ms=map(int,raw_input().split())
ws=map(int,raw_input().split())
hs,hu=map(int,raw_input().split())

xs=[500,1000,1500,2000,2500]
score=0
for i in range(5):
	score+=max(0.3*xs[i],(1-ms[i]/250)*xs[i]-50*ws[i])
print int(score+100*hs-50*hu)
	