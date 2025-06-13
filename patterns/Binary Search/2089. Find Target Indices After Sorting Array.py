# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.


# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/?envType=problem-list-v2&envId=binary-search

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        def find_leftmost(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def find_rightmost(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        left_idx = find_leftmost(nums, target)
        right_idx = find_rightmost(nums, target)

        if left_idx < len(nums) and nums[left_idx] == target:
            return list(range(left_idx, right_idx))
        return []

