# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# https://leetcode.com/problems/longest-harmonious-subsequence/description/?envType=problem-list-v2&envId=sliding-window


from typing import Counter, List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Step 1: Count frequency of each number
        count = Counter(nums)
        max_length = 0
        # Step 2: For each number, check if number+1 exists
        for num in count:
            if num + 1 in count:
                # Step 3: If both num and num+1 exist,
                # the harmonious subsequence length is their frequencies combined
                current_length = count[num] + count[num + 1]
                max_length = max(max_length, current_length)

        return max_length
