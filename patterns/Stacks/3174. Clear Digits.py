# https://leetcode.com/problems/clear-digits/description/?envType=problem-list-v2&envId=stack&difficulty=EASY

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isdigit():
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)
        return "".join(str(x) for x in stack)
