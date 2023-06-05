def majorityElementII(nums):
	freq = {}
	for ele in nums:
		if ele in freq:
			freq[ele]=freq[ele]+1
		else:
			freq[ele]=1
	ans = []
	for key in freq:
		if freq[key]> len(nums)//3:
			ans.append(key)
	return ans