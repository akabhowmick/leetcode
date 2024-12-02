# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/?envType=problem-list-v2&envId=stack&difficulty=EASY

class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            if i == 'D' and len(stack) > 0 and stack[-1]=='C':
                stack.pop()
            elif i == 'B' and len(stack) > 0 and stack[-1]=='A':
                stack.pop()
            else:
                stack.append(i)
        return len(stack)


        