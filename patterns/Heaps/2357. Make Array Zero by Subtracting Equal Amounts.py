# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/description/?envType=problem-list-v2&envId=heap-priority-queue&difficulty=EASY&status=TO_DO

import heapq
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Step 1: Create a min-heap with non-zero elements
        nums = [num for num in nums if num > 0]
        heapq.heapify(nums)

        operations = 0

        # Step 2: Perform operations until the heap is empty
        while nums:
            # Subtract the smallest element from all non-zero elements
            smallest = heapq.heappop(nums)  # Extract smallest non-zero value
            nums = [num - smallest for num in nums if num - smallest > 0]
            heapq.heapify(nums)  # Rebuild the heap with updated values

            # Increment the operation counter
            operations += 1

        return operations
