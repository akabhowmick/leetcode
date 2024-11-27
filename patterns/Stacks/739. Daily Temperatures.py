from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            print(i, temp)
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                results[prev_index] = i - prev_index
            stack.append(i) 

        return results
        