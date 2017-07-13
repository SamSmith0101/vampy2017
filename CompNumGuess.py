lower = 0
upper = 0
guess = 1
ans = ""
while ans !="YEPP":
	ans = input("Is "+str(guess)+" equal to, more, or less than your number (YEPP/MORE/LESS): ")
	if ans == "MORE":
		if upper == 0:
			guess *= 2
		else:
			lower = guess
			guess = int((lower + upper)/2)
	elif ans == "LESS":
		if upper == 0:
			lower = int(guess /2)

		upper = guess
		guess = int((lower + upper)/2)

print("Your number is "+str(guess)+"!")
