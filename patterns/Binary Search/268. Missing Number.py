# https://leetcode.com/problems/missing-number/description/?envType=problem-list-v2&envId=binary-search
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

from typing import List

# Original solution (6/10) - O(n log n) time, O(1) space
class OriginalSolution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] + 1 != nums[i+1]:
                return nums[i] + 1
        if len(nums) not in nums:
            return len(nums)
        if 0 not in nums:
            return 0

# Binary Search Approach - O(n log n) time, O(1) space
class BinarySearchSolution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # If nums[mid] == mid, missing number is to the right
            if nums[mid] == mid:
                left = mid + 1
            # If nums[mid] > mid, missing number is to the left (or is mid)
            else:
                right = mid - 1
        
        return left

# Optimal Mathematical Approach - O(n) time, O(1) space  
class OptimalSolution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Sum of 0 to n = n*(n+1)/2
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# XOR Approach - O(n) time, O(1) space
class XORSolution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n  # Start with n
        
        for i in range(n):
            result ^= i ^ nums[i]
        
        return result

# Set Approach - O(n) time, O(n) space
class SetSolution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i
