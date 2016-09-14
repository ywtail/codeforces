config1=(raw_input()+raw_input()[::-1]).replace("X","")
config2=(raw_input()+raw_input()[::-1]).replace("X","")

if config2==config1 or config2==(config1[1]+config1[2]+config1[0]) or config2==(config1[2]+config1[0]+config1[1]):
	print "YES"
else:
	print "NO"