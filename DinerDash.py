import random
import time

names = ["Abby","Bob","Cyamper","Dylan","Edward","Fred","Geoff","Hailey","Inigo Montoya","Joj","Kaylynn","Lily","Madam Zostra","Newt","Othello","Pidgeon","Quincey"]

Q = []
for name in random.sample(names, 3):
	joining = random.choice(names)
	Q.append(joining)
	print("{0} is joining".format(joining))
		
hour = 1	
while len(Q) > 0:
	time.sleep(6)
	print("It is {0} o' clock, and there are {1} people at the diner!".format(hour, len(Q)))
	for i in range(random.randint(1,5)):
		if len(Q) < 88 and random.uniform(0,1) < 0.50:
			joining = random.choice(names)
			Q.append(joining)
			print("{0} is joining".format(joining))
		elif len(Q) > 0:
			leaving = Q.pop(0)
			print("{0} is leaving!".format(leaving))

	hour += 1

print("Closing up shop!")














