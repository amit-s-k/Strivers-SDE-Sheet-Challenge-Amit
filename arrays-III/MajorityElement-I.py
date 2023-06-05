def findMajorityElement(nums, n):
	freq = {}
	for ele in nums:
		if ele in freq:
			freq[ele]=freq[ele]+1
		else:
			freq[ele]=1
	for key in freq:
		if freq[key]> len(nums)//2:
			return key
	return -1