# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         sorted_s = sorted(s)
#         sorted_t = sorted(t)
#         return sorted_s == sorted_t

# https://leetcode.com/problems/valid-anagram/description/?envType=problem-list-v2&envId=hash-table

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countByLetters = defaultdict(int)
        if len(s) != len(t):
            return False
        # everytime you encounter the letter add it to the dict
        for i in s:
            countByLetters[i] += 1
        # everytime you encounter the letter remove it to the dict
        for i in t:
            countByLetters[i] -= 1
        for val in countByLetters.values():
            if val != 0:
                return False
        return True

        