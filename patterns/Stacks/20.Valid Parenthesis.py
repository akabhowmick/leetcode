# https://leetcode.com/problems/valid-parentheses/description/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Matching pairs
        matching = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in "({[":
                # Push opening brackets onto the stack
                stack.append(char)
            elif char in ")}]":
                # Check for matching opening bracket
                if not stack or stack.pop() != matching[char]:
                    return False

        # If stack is empty, it's balanced
        return len(stack) == 0
