from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit


class Solution:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def mergeIntervals(intervals):
    intervals.sort(key=lambda x: x.start)
    n = len(intervals)
    res = [intervals[0]]
    for i in range(1, n):
        lastMerged = res[-1]
        if intervals[i].start <= lastMerged.end:
            lastMerged.end = max(lastMerged.end, intervals[i].end)
        else:
            res.append(intervals[i])

    return res


n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)
