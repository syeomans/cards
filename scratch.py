import random

start = random.randint(0,4)
for start in range(0,4):
	myList = [start, (start+1)%4, (start+2)%4, (start+3)%4,]
	print(myList)