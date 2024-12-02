# https://leetcode.com/problems/backspace-string-compare/description/?envType=problem-list-v2&envId=stack&difficulty=EASY

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in s:
            if i != '#':
                stack1.append(i)
            else:
                if(len(stack1) > 0):
                    stack1.pop()
        for i in t:
            if i != '#':
                stack2.append(i)
            else:
                if(len(stack2) > 0):
                    stack2.pop()
        return stack1 == stack2
        