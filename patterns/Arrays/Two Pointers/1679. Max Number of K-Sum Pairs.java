// You are given an integer array nums and an integer k.

// In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
// Return the maximum number of operations you can perform on the array.

// https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75

import java.util.Arrays;

class Solution {

    public int maxOperations(int[] nums, int k) {
        if (nums.length <= 0) {
            return 0;
        }
        int answer = 0;
        Arrays.sort(nums);
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            if (nums[left] + nums[right] == k) {
                answer++;
                left++;
                right--;
            } else {
                if (nums[left] + nums[right] > k) {
                    right--;
                } else {
                    left++;
                }
            }

        }
        return answer;
    }
}
