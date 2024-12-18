import heapq
import math
from typing import List


# https://leetcode.com/problems/take-gifts-from-the-richest-pile/?envType=problem-list-v2&envId=heap-priority-queue&difficulty=EASY

# You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

# Choose the pile with the maximum number of gifts.
# If there is more than one pile with the maximum number of gifts, choose any.
# Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
# Return the number of gifts remaining after k seconds.


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        print(gifts)
        heapq.heapify(gifts)
        counter = 0
        while counter < k:
            value = -1 * heapq.heappop(gifts)
            print(value)
            heapq.heappush(gifts, -1 * math.floor(math.sqrt(value)))
            counter += 1

        sum = 0
        for i in gifts:
            sum += i
        return -sum
