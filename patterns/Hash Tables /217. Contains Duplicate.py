# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=hash-table

# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for i in nums:
            if i in hash:
                return True
            hash.add(i)
        return False
