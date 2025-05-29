# https://leetcode.com/problems/sort-colors/?envType=problem-list-v2&envId=two-pointers

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_counter = 0
        one_counter = 0
        two_counter = 0
        for num in nums:
            if num == 0:
                zero_counter +=1
            if num == 1:
                one_counter +=1
            if num == 2:
                two_counter +=1
        for i in range(len(nums)):
            if i < zero_counter:
                nums[i] = 0
            elif i < zero_counter + one_counter:
                nums[i] = 1
            else:
                nums[i] = 2