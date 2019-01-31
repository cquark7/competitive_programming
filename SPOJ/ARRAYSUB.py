from collections import deque
from sys import stdout


def maxSlidingWindow(nums, k):
    d = deque()
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            stdout.write("%d " % nums[d[0]])


n = int(input())
arr = list(map(int, input().split()))
k = int(input())
maxSlidingWindow(arr, k)
