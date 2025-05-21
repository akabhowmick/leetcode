# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_window = float('inf')

        for right in range(len(nums)):
            total += nums[right]
            while total >= target: 
                min_window = min(min_window, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_window == float('inf') else min_window
        