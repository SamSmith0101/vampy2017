def tree(child):
	return [None, child, None]

def data(node, child=None):
	if node is None: 
		return None
	elif val is None:
		return node[1]
	else:
		node[1] = child
		
def yes(node, child = None):
	if node is None:
		return None
	elif val is None:
		return node[0]
	else:
		node[0] = [None, child, None]

def no(node, child = None):
	if node is None:
		return None
	elif val is None
		return node[2]
	else:
		node[2] = [None, child, None]

root = tree("Am I an object or a place? (YES/NO): ")
yes(root, tree("Am I bigger than a PC? (YES/NO): "))

no(root, tree("Am I human? (YES/NO): "))

yes(yes(root), tree("Am I a building? (YES/NO): "))
no(yes(root), tree("Am I consumed as you use me? (YES/NO): "))

yes(no(root), tree("Am I fictional? (YES/NO): "))
no(no(root), tree("Can you fit me in a coffee mug? (YES/NO): "))

yes(yes(yes(root)), tree("Am I a salon? (YES/NO): "))
no(yes(yes(root)), tree("Am I New York? (YES/NO): "))
yes(no(yes(root)), tree("Am I pizza? (YES/NO): "))
no(no(yes(root)), tree("Am I a hat? (YES/NO): "))

yes(yes(no(root)), tree("Am I Santa Claus? (YES/NO): "))
no(yes(no(root)), tree("Am I MJ? (YES/NO): "))
yes(no(no(root)), tree("Am I a rat? (YES/NO): "))
no(no(no(root)), tree("Am I Dracula? (YES/NO): "))

yes(yes(yes(yes(root))), tree("Salon!"))
yes(no(yes(yes(root))), tree("New York!"))
yes(yes(no(yes(root))), tree("Pizza!"))
yes(no(no(yes(root))), tree("Hat!))
yes(yes(yes(no(root))), tree("Santa Claus!"))
yes(no(yes(no(root))), tree("MJ!"))
yes(yes(no(no(root))), tree("Rat!"))
yes(no(no(no(root))), tree("Dracula!"))
no(yes(yes(yes(root)), tree("Bowling Alley!"))
no(no(yes(yes(root))), tree("Umbrella!"))
no(yes(no(yes(root))), tree("Bar of Soap!"))
no(no(no(yes(root))), tree("Computer!"))
no(yes(yes(no(root))), tree("James Bond!"))
no(no(yes(no(root))), tree("Brittany Spears!"))
no(yes(no(no(root))), tree("Frog!"))
no(no(no(no(root))), tree("Chicken!"))

tracker = root 
while "?" in data(tracker):
	answer = input(data(tracker))
	if answer == "YES":
		tracker = yes(tracker)
	else:
		tracker = no(tracker)

print(data(tracker))

