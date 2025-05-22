import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Minimum possible speed (slowest)
        minSpeed = 1
        # Maximum possible speed (fastest)
        maxSpeed = max(piles)
        # Best speed found so far
        bestSpeed = maxSpeed  # since worst case is eating the biggest pile per hour

        while minSpeed <= maxSpeed:
            mediumSpeed = (minSpeed + maxSpeed) // 2
            totalHours = 0

            # Calculate hours needed at current mediumSpeed
            for pile in piles:
                totalHours += math.ceil(pile / mediumSpeed)

            # If within time limit, try to go slower
            if totalHours <= h:
                bestSpeed = mediumSpeed  # save this as a possible answer
                maxSpeed = mediumSpeed - 1
            else:
                minSpeed = mediumSpeed + 1

        return bestSpeed
      
# https://leetcode.com/problems/koko-eating-bananas/?envType=study-plan-v2&envId=leetcode-75

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.