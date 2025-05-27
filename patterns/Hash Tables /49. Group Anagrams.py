# https://leetcode.com/problems/group-anagrams/description/?envType=problem-list-v2&envId=hash-table
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.


from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countByNumbers = {}
        for i in nums:
            if i in countByNumbers:
                countByNumbers[i] += 1
            else:
                countByNumbers[i] = 1
        sorteddict = dict(sorted(countByNumbers.items(), key=lambda item: item[1]))
        sortlist = list(sorteddict.keys())
        sortlist = sortlist[::-1]
        return sortlist[0:k]
