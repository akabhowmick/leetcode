# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
# https://leetcode.com/problems/remove-k-digits/description/?envType=problem-list-v2&envId=stack


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for n in num:
            while st and k and st[-1] > n:
                st.pop()
                k -= 1
            if st or n is not "0":
                st.append(n)

        if k:
            st = st[0:-k]

        return "".join(st) or "0"
