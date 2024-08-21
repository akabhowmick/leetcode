# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
# Tags: Arrays Two Pointers


from typing import List


class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        non_zero_index = 0

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[non_zero_index] = arr[i]
                non_zero_index += 1

        for i in range(non_zero_index, len(arr)):
            arr[i] = 0
