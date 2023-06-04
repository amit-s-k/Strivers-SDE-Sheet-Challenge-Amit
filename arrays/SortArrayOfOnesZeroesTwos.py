from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


def sort012(nums, n):
    onesCount = 0
    zeroCount = 0
    for ele in nums:
        if ele == 0:
            zeroCount += 1
        elif ele == 1:
            onesCount += 1
    i = 0
    while i < zeroCount:
        nums[i] = 0
        i += 1
    k = i
    while k < i + onesCount:
        nums[k] = 1
        k += 1
    m = k
    while m < len(nums):
        nums[m] = 2
        m += 1
if __name__=="__main__":
    nums = [1,1,2,0,2,1,0]
    sort012(nums,len(nums))
    print(nums)


