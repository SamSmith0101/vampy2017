def mode(nums):
	tally = {}
	M = nums[0]
	for x in nums:
		tally[x] = tally.get(x, 0) + 1
		if tally[x] > tally[M]:
			M = x
	return M

#print("The mode is "+str(mode([1, 8, 7, 12, 2, -5, 0, 1, 1, 2])))

def maximum(nums):
	M = nums[0]
	for x in nums:
		if x > M:
			M = x

	return M

def minimum(nums):
	M = nums[0]
	for x in nums:
		if x < M:
			M = x

	return M

def mean(nums):
	if lens(nums) == 0:
		return None

	M = 0
	for x in nums:
		M += x

	M /= len(nums)
	return M


def median(nums):
	temp = sorted(nums)
	if len(temp) % 2 == 0:
		mid1 = int(len(temp)/2)
		mid2 = int(len(temp)/2)
		return (temp[med1] + temp[mid2])/2
	else:
		mid = int(len(temp)/2)
		return temp[mid]
	
	
	
