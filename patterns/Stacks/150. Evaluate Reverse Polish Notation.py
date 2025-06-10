# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=problem-list-v2&envId=stack


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                number_one = stack.pop()
                number_two = stack.pop()
                stack.append(number_two + number_one)
            elif i == "-":
                number_one = stack.pop()
                number_two = stack.pop()
                stack.append(number_two - number_one)
            elif i == "*":
                number_one = stack.pop()
                number_two = stack.pop()
                stack.append(number_two * number_one)
            elif i == "/":
                number_one = stack.pop()
                number_two = stack.pop()
                stack.append(int(number_two / number_one))
            else:
                stack.append(int(i))
        return stack.pop()
