# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/description/?envType=problem-list-v2&envId=heap-priority-queue&difficulty=EASY&status=TO_DO


import heapq


class Solution:
    def largestInteger(self, num: int) -> int:
        even = []
        odd = []
        nums = [-int(n) for n in str(num)]
        for n in nums:
            if n % 2:
                heapq.heappush(even, n)
            else:
                heapq.heappush(odd, n)

        res = 0
        for n in nums:
            if n % 2:
                x = -heapq.heappop(even)
            else:
                x = -heapq.heappop(odd)
            res = res * 10 + x

        return res
