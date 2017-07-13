print("Setting up the graph data structure...")
connections = {}
connections["Joj"] = []
connections["Emily"] = ["Joj","Jeph","Jeff"]
connections["Jeph"] = ["Joj","Geoff"]
connections["Jeff"] = ["Joj","Judge"]
connections["Geoff"] = ["Joj","Jebb"]
connections["Jebb"] = ["Joj","Emily"]
connections["Judge"] = ["Joj","Judy"]
connections["Jodge"] = ["Joj","Jebb","Stephen","Judy"]
connections["Judy"] = ["Joj","Juge"]
connections["Stephen"] = ["Joj","Jodge"]

names = ["Joj","Emily","Jeph","Jeff","Geoff","Jebb","Judge","Jodge","Judy","Stephen"]

candidate = names[0]


print("Finding the celebrity candidate...")
for i in range(1, len(names)):
	if names[i] in connections[candidate]:
		candidate = names[i]

print("OUR BEST CANDIDATE IS {0}".format(candidate))

print("Verifying the candidate 1/2")
for name in names:
	if name != candidate and name in connections[candidate]:
		print("The candidate is a lie!!!!!!!!! They know somebody!!!")
	elif candidate not in connections[name]:
		print("The candidate is a lie!!!!!!!!!!!! They are not known by somebody!!!!!")
		exit()
		
print("We made it to the end, the celebrity is the real deal =D")

