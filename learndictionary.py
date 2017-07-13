d = {"age":12}
d["name"] = "Sam"

print(d["age"])
print(d["name"])

#merge two dictionaries
d1 = {"key1":155,"key2":123,"key3":142}
d2 = {"key4":12,"key5":13,"key6":123}

def multiply_dictionary(dictionary, multiple):
	for key in dictionary:
		dictionary[key] *= multiple
	print(dictionary)

print(sorted(d1))
sorted_keys = sorted(d1)
for key in sorted_keys:
	print(d1[key])
