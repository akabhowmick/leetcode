# You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

# Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.

# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/?envType=problem-list-v2&envId=prefix-sum

import heapq
from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        sums = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                sums.append(current_sum)
        sums.sort()
        return sum(sums[left - 1 : right]) % MOD

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
        Optimized O(n²) solution using min-heap
        Only generates the smallest (right) subarray sums instead of all n²(n+1)/2 sums
        """
        MOD = 10**9 + 7

        # Min-heap: (sum, start_index, end_index)
        heap = []

        # Initialize heap with all single-element subarrays
        for i in range(n):
            heapq.heappush(heap, (nums[i], i, i))

        result = 0

        # Extract the smallest 'right' sums
        for rank in range(1, right + 1):
            current_sum, start, end = heapq.heappop(heap)

            # If this sum is within our target range [left, right]
            if rank >= left:
                result = (result + current_sum) % MOD

            # Extend the subarray to the right if possible
            if end + 1 < n:
                new_sum = current_sum + nums[end + 1]
                heapq.heappush(heap, (new_sum, start, end + 1))

        return result
