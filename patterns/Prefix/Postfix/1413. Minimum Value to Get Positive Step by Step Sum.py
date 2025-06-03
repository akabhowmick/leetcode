# Given an array of integers nums, you start with an initial positive value startValue.

# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/?envType=problem-list-v2&envId=prefix-sum

# 1. Calculate all prefix sums assuming startValue = 0
# 2. Find the minimum prefix sum
# 3. If the minimum is negative, we need startValue to offset it
# 4. The result must be at least 1 (positive requirement)

from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = 0
        curr_sum = 0 
        for num in nums:
            curr_sum += num
            min_sum = min(min_sum, curr_sum)
        return max(1, 1 - min_sum)
        