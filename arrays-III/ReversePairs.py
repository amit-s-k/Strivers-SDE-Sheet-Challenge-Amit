def reversePairs(nums, n):
    return mergeSort(nums,0,len(nums)-1)
def mergeSort( nums,low,high):
    if low>=high:
        return 0
    mid = int((low+high)/2)
    count = mergeSort(nums,low,mid)
    count += mergeSort(nums,mid+1,high)
    count +=merge(nums,low,mid,high)
    return count
def merge(nums,low,mid,high):
    count = 0
    j=mid+1
    for i in range(low,mid+1):
        while j <= high and nums[i] > 2 * nums[j]:
            j+=1
        count += j-(mid+1)
    temp = []
    left = low
    right = mid+1
    while left<=mid and right <=high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1
    while left<=mid:
        temp.append(nums[left])
        left+=1
    while right <=high:
        temp.append(nums[right])
        right+=1
    for k in range(low,high+1):
        nums[k]=temp[k-low]
    return count
if __name__=="__main__":
    nums=[1,2,3,2,3,1]

    print(reversePairs(nums,len(nums)))