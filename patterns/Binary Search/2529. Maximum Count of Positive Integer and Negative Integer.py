# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/?envType=problem-list-v2&envId=binary-search

from typing import List


class Solution:
    
    def maximumCount(self, nums: List[int]) -> int:
        def findFirstNonNegative():
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= 0:
                    right = mid
                else:
                    left = mid + 1
            return left
        def findFirstPositive():
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > 0:
                    right = mid
                else:
                    left = mid + 1
            return left

        first_non_negative = findFirstNonNegative()
        first_positive = findFirstPositive()
        
        negative_count = first_non_negative  
        positive_count = len(nums) - first_positive  
        
        return max(negative_count, positive_count)
 
        

