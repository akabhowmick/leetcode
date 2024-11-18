# Write a function to find the longest common prefix string amongst an array of strings.
# https://leetcode.com/problems/longest-common-prefix/description/


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = ""
        strs = sorted(strs)
        first_word = strs[0]
        last_word = strs[-1]
        for i in range(min(len(first_word), len(last_word))):
            if first_word[i] != last_word[i]:
                return prefix
            prefix += first_word[i]
        return prefix


# 2nd approach
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Iterate over the other strings in the list
        for s in strs[1:]:
            # Reduce the prefix until it matches the beginning of s
            while not s.startswith(prefix):
                # Shorten the prefix by removing the last character
                prefix = prefix[:-1]
                # If the prefix becomes empty, return ""
                if not prefix:
                    return ""

        return prefix
        
# Explanation
# Initialization: The first string is used as the initial prefix.
# Comparison: For each subsequent string, check if it starts with the current prefix:
# If it doesn't, truncate the prefix from the end until a match is found.
# If the prefix becomes empty, return an empty string.
# Result: The remaining prefix is the longest common prefix among all strings.
# Complexity Analysis
# Time Complexity: O(S), where S is the sum of all characters in all strings. In the worst case, we might have to check every character of every string.
# Space Complexity: O(1), since we're only using a few extra variables to store the prefix.
