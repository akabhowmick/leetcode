// Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
// https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75
// Time complexity O(n); Space complexity O(n)
// Tags Arrays Hash Maps

import java.util.HashMap;
import java.util.HashSet;

class Solution {

    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> charCounter = new HashMap<>();
        for (int i : arr) {
            charCounter.put(i, charCounter.getOrDefault(i, 0) + 1);
        }
        HashSet<Integer> uniqueCounts = new HashSet<>();
        for (int count : charCounter.values()) {
            if (!uniqueCounts.add(count)) {
                return false;
            }
        }
        return true;
    }
}
