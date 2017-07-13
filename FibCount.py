def countfast(N):
	counts = [0, 0]
	for i in range(2, N+1):
		counts.append(counts[i-1]+count[i-2]+1)
	return

def fast_fib(N):
	counts = [0,1]
		for i in range(2,N+1):
			counts.append(counts[i-1]+counts[i-2])
	return counts[N]

