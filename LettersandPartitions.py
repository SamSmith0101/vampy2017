import functools

def letters(K):
	qwerty = "QWERTYUIOPASDFGHJKLZXCVBNM"
	def solve(K, start, Z):
		if K == 0:
			print(Z)
		else:
			for i in range(start, len(qwerty)-K+1):
				solve(K-1, i+1, Z+qwerty[i])

	solve(K, 0, "")

def partitions(K):
	qwerty = "QWERTYUIOPASDFGHJKLZXCVBNM"
	def solve(K, start, Z):
		if K == i:
			print(Z+"/"+qwerty[start:]+"/")
		else:
			for i in range(start+1, len(qwerty)-K+2):
				solve(K-1, i, Z+"/"+qwerty[start:i])
	solve(K, 0, "")
	
partitions(4)
