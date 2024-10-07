// https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75

// Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

// Space 0(1)
// Runtime 0(n)

class Solution {

    public int longestOnes(int[] nums, int k) {
        int left = 0;  // Left pointer of the window
        int maxLength = 0;  // To store the maximum length of the subarray
        int zeroCount = 0;  // To track the number of 0s in the window

        // Iterate through the array with the right pointer
        for (int right = 0; right < nums.length; right++) {
            // If we encounter a 0, increment the zero count
            if (nums[right] == 0) {
                zeroCount++;
            }

            // If the number of 0s exceeds k, move the left pointer to reduce the window size
            while (zeroCount > k) {
                if (nums[left] == 0) {
                    zeroCount--;
                }
                left++;
            }

            // Update the maximum length of the subarray with at most k 0s
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }

}
