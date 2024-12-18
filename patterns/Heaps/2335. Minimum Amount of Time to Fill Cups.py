# 2335. Minimum Amount of Time to Fill Cups

# You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

# You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed to fill up all the cups.

# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/description/?envType=problem-list-v2&envId=heap-priority-queue&difficulty=EASY

import heapq
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        #make a make maxheap by doing negative elements 
        pq = [-q for q in amount if q != 0]
        heapq.heapify(pq)
        ret = 0

        while len(pq) > 1:
            first = heapq.heappop(pq)
            second = heapq.heappop(pq)
            first += 1
            second += 1
            ret += 1
            if first:
                heapq.heappush(pq, first)
            if second:
                heapq.heappush(pq, second)

        if pq:
            return ret - pq[0]
        else:
            return ret
          
# Test:
amount = [1,4,2]
print(Solution().fillCups(amount)) # Output: 4