# https://leetcode.com/problems/reverse-prefix-of-word/description/?envType=problem-list-v2&envId=stack&difficulty=EASY


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack1 = []
        stack2 = []
        foundch = False
        for i in word:
            if i != ch and len(stack2) == 0:
                stack1.append(i)
            elif i == ch:
                foundch = True
                stack2.append(i)
                while stack1:
                    char = stack1.pop()
                    stack2.append(char)
            else:
                stack2.append(i)
        if foundch == False:
            print(stack1)
            return "".join(str(x) for x in stack1)
        return "".join(str(x) for x in stack2)
