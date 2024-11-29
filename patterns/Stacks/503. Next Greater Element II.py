# https://leetcode.com/problems/next-greater-element-ii/

# Algorithm
# Traverse the array twice (using modulo arithmetic to handle circular behavior).
# Maintain a stack of indices where the next greater element is not yet found.
# Compare the current number with the number corresponding to the index on top of the stack:
# If the current number is greater, pop from the stack and update the result for the popped index.
# Push the current index onto the stack for future comparisons.


from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                prev_index = stack.pop()
                result[prev_index] = nums[i % n]
            if i < n:
                stack.append(i)

        return result
