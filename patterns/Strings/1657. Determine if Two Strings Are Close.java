// https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75

// Two strings are considered close if you can attain one from the other using the following operations:
// Operation 1: Swap any two existing characters.
// For example, abcde -> aecdb
// Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
// For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
// You can use the operations on either string as many times as necessary.
// Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

// O(1) space O(n) runtime 
// Hash Table String Sorting Counting

import java.util.Arrays;

class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }

        int[] freq1 = new int[26];
        int[] freq2 = new int[26];

        // Create boolean arrays to track which characters are present
        boolean[] chars1 = new boolean[26];
        boolean[] chars2 = new boolean[26];

        // Count frequency and record presence of characters in word1 and word2
        for (char c : word1.toCharArray()) {
            freq1[c - 'a']++;
            chars1[c - 'a'] = true;
        }

        for (char c : word2.toCharArray()) {
            freq2[c - 'a']++;
            chars2[c - 'a'] = true;
        }

        // Check if both words have the same set of characters
        for (int i = 0; i < 26; i++) {
            if (chars1[i] != chars2[i]) {
                return false;
            }
        }

        // Sort the frequency arrays to check if both words can be transformed
        Arrays.sort(freq1);
        Arrays.sort(freq2);

        // Check if both words have the same frequency counts
        return Arrays.equals(freq1, freq2);
    }

}
