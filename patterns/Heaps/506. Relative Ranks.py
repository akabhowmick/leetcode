# https://leetcode.com/problems/relative-ranks/?envType=problem-list-v2&envId=heap-priority-queue&difficulty=EASY


import heapq
from typing import List


class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:

        n = len(score)
        # Step 1: Create a max-heap with negated scores
        max_heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(max_heap)

        # Step 2: Prepare the result array
        result = [""] * n
        rank = 1

        # Step 3: Pop elements from the heap and assign ranks
        while max_heap:
            _, index = heapq.heappop(max_heap)
            if rank == 1:
                result[index] = "Gold Medal"
            elif rank == 2:
                result[index] = "Silver Medal"
            elif rank == 3:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank)
            rank += 1

        return result
