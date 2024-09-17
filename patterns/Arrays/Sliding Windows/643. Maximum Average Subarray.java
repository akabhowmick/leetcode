// https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

// You are given an integer array nums consisting of n elements, and an integer k.

// Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

//Tags: O(n) Space 0(n) 


class Solution {

    public double findMaxAverage(int[] nums, int k) {
        // Compute the sum of the first 'k' elements
        double currentSum = 0;
        for (int i = 0; i < k; i++) {
            currentSum += nums[i];
        }

        // Initialize maxAverage with the average of the first subarray
        double maxAverage = currentSum / k;

        // Slide the window over the array
        for (int i = k; i < nums.length; i++) {
            currentSum += nums[i] - nums[i - k]; // Add the new element, remove the old one
            maxAverage = Math.max(maxAverage, currentSum / k);
        }

        return maxAverage;
    }
}
