# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# https://leetcode.com/problems/top-k-frequent-elements/description/?envType=problem-list-v2&envId=hash-table


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
        # countByNumbers.items() gives key-value pairs (number, frequency).
        # key=lambda item: item[1] sorts by the frequency.
        # This returns a list of tuples, sorted in ascending order of frequency 
        sortlist = list(sorteddict.keys())
        # convert the keys into a list
        sortlist = sortlist[::-1]
        #Reverse it to get descending order:
        return sortlist[0:k]
      
      
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # Step 1: Count frequency
#         count = {}
#         for num in nums:
#             count[num] = count.get(num, 0) + 1

#         # Step 2: Sort by frequency (value) in descending order
#         sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)

#         # Step 3: Extract only the top k keys
#         return [item[0] for item in sorted_items[:k]]


# sorted(iterable, key=..., reverse=...)
# iterable: list, tuple, or dict items

# key: a function that returns a value to sort by

# reverse=True: sort descending
