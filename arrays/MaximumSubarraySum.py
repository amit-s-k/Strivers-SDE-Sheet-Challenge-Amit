from os import *
from sys import *
from collections import *
import math

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(nums, n) :
    currSum = 0
    maxSum = -math.inf
    for i in range(n):
        currSum=max(currSum+nums[i],0)
        maxSum=max(maxSum,currSum)
    return maxSum
if __name__ =="__main__":
    nums= [-1,-1,-2]
    print(maxSubarraySum(nums,len(nums)))