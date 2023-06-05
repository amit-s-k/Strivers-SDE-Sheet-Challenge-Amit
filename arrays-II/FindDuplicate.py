def findDuplicate(nums:list, n:int):
    i = 0
    while True:
        if nums[i] < 0:
            return i
        temp = nums[i]
        nums[i]=-nums[i]
        i=temp