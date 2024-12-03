# https://leetcode.com/problems/last-stone-weight/?envType=problem-list-v2&envId=heap-priority-queue&difficulty=EASY

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first > second:
                heapq.heappush(stones, -1 * (first - second))

        if len(stones) == 0:
            return 0

        return abs(stones[0])
