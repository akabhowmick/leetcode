# You are given an integer array nums, an integer k, and an integer multiplier.

# You need to perform k operations on nums. In each operation:

# Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.

# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/?envType=problem-list-v2&envId=heap-priority-queue&difficulty=EASY

from heapq import heappush
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Priority queue (min-heap) to store pairs of (value, index)
        pq = []
        for i, num in enumerate(nums):
            heappush(pq, (num, i))

        # Perform k operations
        while k > 0:
            value, idx = heappop(pq)  # Get the smallest element
            value *= multiplier  # Multiply the value
            heappush(pq, (value, idx))  # Push it back to the heap
            k -= 1

        # Update the original array with the final values from the heap
        while pq:
            value, idx = heappop(pq)
            nums[idx] = value

        return nums
