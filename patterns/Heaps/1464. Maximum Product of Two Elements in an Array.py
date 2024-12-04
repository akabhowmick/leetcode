# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/?envType=problem-list-v2&envId=heap-priority-queue&difficulty=EASY&status=TO_DO


# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

import heapq
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        num1 = -1 * heapq.heappop(nums) - 1
        num2 = -1 * heapq.heappop(nums) - 1
        return num1 * num2
