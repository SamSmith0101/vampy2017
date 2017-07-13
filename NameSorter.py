import Sorting

read_filename = "/home/vampy/data/test1"
write_filename = "/home/vampy/data/test2"

fp = open(filename, "r")
N = int(fp.readline())
names = []
for i in range(N):
	names.append(fp.readline().strip())
	
fp.close()

Sorting.mergesort(names)

fp = open(write_filename, "w")
fp.write("{0}\n".format(N))
for i in range(N):
	fp.write("{0}\n".format(names[i]))

fp.close()
