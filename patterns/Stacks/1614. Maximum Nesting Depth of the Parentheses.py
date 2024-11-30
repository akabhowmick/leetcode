# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/?envType=problem-list-v2&envId=stack&difficulty=EASY

# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_len = 0
        for char in s:
            if len(stack) > max_len:
                max_len = len(stack)
            if char == "(":
                stack.append(char)
            elif char == ")":
                stack.pop()
        return max_len
