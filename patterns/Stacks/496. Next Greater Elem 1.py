# 496. Next Greater Element I

# https://leetcode.com/problems/next-greater-element-i/description/


from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        # Build the next_greater dictionary in reverse order of nums2
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Fill the next_greater dictionary for remaining elements in nums1 with -1
        while stack:
            next_greater[stack.pop()] = -1

        return [next_greater[num] for num in nums1]
