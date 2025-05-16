// https://leetcode.com/problems/range-sum-query-immutable/description/
// Difficulty: Easy
// tags: prefix

// Solution
// O(n) time to create the prefix array, O(1) time to query it, O(n) space to store the prefix array, but if we don't need nums anymore we could consider it O(1) space. Iterate over nums and create a prefixArray, representing the current tallied sum, including the current number. When we query a range, say: [1, 2, 3] and we query indices [1,2] inclusive, we take the sum of indices [0,2] inclusve, and the sum of indices [0,0] inclusive, and subtract the latter from the former to get the sum of the range
class NumArray {

    public int[] arr2;

    public NumArray(int[] nums) {
        arr2 = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            arr2[i + 1] = arr2[i] + nums[i];
        }
    }

    public int sumRange(int left, int right) {
        return arr2[right + 1] - arr2[left];
    }
}
