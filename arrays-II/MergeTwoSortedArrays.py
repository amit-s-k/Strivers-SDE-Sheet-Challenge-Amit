def ninjaAndSortedArrays(nums1,nums2,m,n):
    # Write your code here.
    p1 = m-1
    p2= n-1
    p=m+n-1

    while p>=0:
        if p2 <0:
            break
        if p1 >=0 and nums1[p1] > nums2[p2]:
            nums1[p]=nums1[p1]
            p1-=1
        else:
            nums1[p]=nums2[p2]
            p2-=1
        p-=1
    return nums1
if __name__=="__main__":
    nums1= [3,6,9,0,0]
    nums2 = [4,10]
    print(ninjaAndSortedArrays(nums1,nums2,len(nums1)-len(nums2),len(nums2)))