answer = input("Am I an object or a place? YES/NO: ")
if answer == "YES":
	answer = input("Am I bigger than a PC? YES/NO: ")
	if answer == "YES":
		answer = input("Am I a building? YES/NO: ")
		if answer == "YES":
			answer = input("Am I a salon? YES/NO: ")
			if answer == "YES":
				print("I am a salon")
			else:
				print("I am a bowling alley")
		else:
			answer = input("Am I New York? YES/NO: ")
			if answer == "YES":
				print("I am New York")
			else:
				print("I am an umbrella")
	else:
		answer = input("Am I consumed as you use me? YES/NO: ")
		if answer == "YES":
			answer = input("Am I a pizza? YES/NO: ")
			if answer == "YES":
				print("I am a pizza")
			else:
				print("I am a bar of soap")
		else:
			answer = input("Am I a hat? YES/NO: ")
			if answer == "YES":
				print("I am a hat")
			else:
				print("I am a computer")
else:
	answer = input("Am I am human? YES/NO: ")
	if answer == "YES":
		answer = input("Am I fictional? YES/NO: ")
		if answer == "YES":
			answer = input("Am I Santa Claus? YES/NO: ")
			if answer == "YES":
				print("I am Santa Claus")
			else:
				print("I am James Bond")
		else:
			answer = input("Am I Brittany Spears? YES/NO: ")
			if answer == "YES":
				print("I am Brittany Spears")
			else:
				print("I am Michael Jackson")
	else:
		answer = input("Could you fit me in a coffee mug? YES/NO: ")
		if answer == "YES":
			answer = input("Am I a frog? YES/NO: ")
			if answer == "YES":
				print("I am a frog")
			else:
				print("I am a rat")
		else:
			answer = input("Am I Dracula? YES/NO: ")
			if answer == "YES":
				print("I am Dracula")
			else:
				print("I am a chicken")
