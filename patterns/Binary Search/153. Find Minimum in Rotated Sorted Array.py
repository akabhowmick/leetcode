# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.

#   https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=binary-search


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # Compare mid with right to determine which half to search
            if nums[mid] > nums[right]:
                # Minimum is in right half (mid+1 to right)
                left = mid + 1
            else:
                # Minimum is in left half (left to mid)
                right = mid
        return nums[left]
