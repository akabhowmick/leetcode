// https://leetcode.com/problems/find-pivot-index/description/
// Difficulty: Easy
// tags: prefix / postfix

// Solution
// O(n) time and O(1) space. Maintain a prefix sum and postfix sum. Iterate over the array and check if the prefix sum is equal to the postfix sum. If so, return the index. Otherwise, increment the prefix sum and decrement the postfix sum
class Solution {

    public int pivotIndex(int[] nums) {
        int[] leftSums = new int[nums.length];
        int[] rightSums = new int[nums.length];
        // left sums 
        for (int i = 1; i < nums.length; i++) {
            leftSums[i] = leftSums[i - 1] + nums[i - 1];
        }
        // right sums 
        for (int i = nums.length - 2; i > -1; i--) {
            rightSums[i] = rightSums[i + 1] + nums[i + 1];
        }
        // check if there is a match
        for (int i = 0; i < nums.length; i++) {
            if (rightSums[i] == leftSums[i]) {
                return i;
            }
        }
        return -1;
    }
}
