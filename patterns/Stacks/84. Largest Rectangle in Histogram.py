# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# https://leetcode.com/problems/largest-rectangle-in-histogram/description/?envType=problem-list-v2&envId=stack


from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Step 1: Initialization
        stack = [-1]
        max_area = 0

        # Step 2: Process Each Bar (Left to Right)
        for i in range(len(heights)):
            # Step 3: Maintain Monotonic Stack
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            # Step 4: Add Current Bar
            stack.append(i)

        # Step 5: Process Remaining Bars
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area
