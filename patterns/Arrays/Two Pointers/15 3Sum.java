// https://leetcode.com/problems/3sum/description/

// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.

// O(n^2) uses the two pointer solution 

// O(n^3) original solution with 3 for loops but that is not great 

class Solution {
  public List<List<Integer>> threeSum(int[] nums) {
      List<List<Integer>> answer = new ArrayList<>();
      // if less than 3 then return empty 
      if (nums == null || nums.length < 3) {
          return answer;
      }
      
      // Sort the array first
      Arrays.sort(nums);
      
      // Iterate through the array
      for (int i = 0; i < nums.length - 2; i++) {
          // Skip duplicate elements
          if (i > 0 && nums[i] == nums[i - 1]) {
              continue;
          }
          
          int left = i + 1;
          int right = nums.length - 1;
          
          while (left < right) {
              int sum = nums[i] + nums[left] + nums[right];
              
              if (sum == 0) {
                  answer.add(Arrays.asList(nums[i], nums[left], nums[right]));
                  
                  // Move left and right pointers to the next different elements
                  while (left < right && nums[left] == nums[left + 1]) {
                      left++;
                  }
                  while (left < right && nums[right] == nums[right - 1]) {
                      right--;
                  }
                  
                  left++;
                  right--;
              } else if (sum < 0) {
                  left++; // We need a larger sum, move left pointer to the right
              } else {
                  right--; // We need a smaller sum, move right pointer to the left
              }
          }
      }
      
      return answer;
  }
}

// Sorting: First, sort the array. This allows us to efficiently use a two-pointer technique to find pairs that sum to a specific target.

// Two-pointer technique: For each element in the array, consider it as the first element of the triplet. Then, use two pointers to find the other two elements that sum up to zero.
// Initialize the left pointer just after the current element and the right pointer at the end of the array.
// Move the left pointer to the right or the right pointer to the left depending on whether the sum is less than or greater than zero.
// If the sum is zero, add the triplet to the result set.

// Avoid duplicates: To ensure the result contains unique triplets, skip duplicate elements both for the current element and the two pointers.