cd=raw_input()
if "a"<cd[0]<"h" and "1"<cd[1]<"8":
	print 8
elif cd=="a8" or cd=="a1" or cd=="h8" or cd=="h1":
	print 3
else:
	print 5