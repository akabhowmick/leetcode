# https://leetcode.com/problems/group-anagrams/description/?envType=problem-list-v2&envId=hash-table
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())
        