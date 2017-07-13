d1 = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}
d2 = {"key4":12,"key5":13,"key3":123}

sorted_keys = sorted(d1)
print(sorted_keys)

for key in sorted_keys:
	print(d1[key])
