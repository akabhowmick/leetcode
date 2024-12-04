# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/?envType=problem-list-v2&envId=heap-priority-queue&difficulty=EASY


import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []

        # Step 1: Calculate the soldier count for each row and store in heap
        for index, row in enumerate(mat):
            soldier_count = sum(row)  # Count the number of 1s in the row
            heapq.heappush(
                heap, (soldier_count, index)
            )  # Push (count, index) into the heap

        # Step 2: Extract the indices of the k weakest rows
        result = []
        for _ in range(k):
            _, idx = heapq.heappop(heap)  # Pop the smallest element
            result.append(idx)

        return result
