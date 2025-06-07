# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=problem-list-v2&envId=binary-search


from typing import List


class OriginalSolution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1 and target == nums[0]:  # Unnecessary edge case
            return [0, 0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                initial_pos = ending_pos = mid
                # Linear expansion - can be O(n) in worst case
                while initial_pos >= 0 and nums[initial_pos] == target:
                    initial_pos -= 1
                while ending_pos < len(nums) and nums[ending_pos] == target:
                    ending_pos += 1
                return [initial_pos + 1, ending_pos - 1]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]


# Optimal solution (10/10) - Two binary searches
class OptimalSolution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    right = mid - 1  # Continue searching left for first occurrence
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return result

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    left = mid + 1  # Continue searching right for last occurrence
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return result

        first = findFirst(nums, target)
        if first == -1:
            return [-1, -1]
        last = findLast(nums, target)
        return [first, last]
