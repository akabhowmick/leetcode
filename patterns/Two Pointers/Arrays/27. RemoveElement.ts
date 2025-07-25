// Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

// Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

// Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
// Return k.

// https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

// Topics: Array, Two-Pointers

function removeElement(nums: number[], val: number): number {
  let k = 0;
  for (let i = 0; i < nums.length; i++){
      if (nums[i] !== val){
          nums[k] = nums[i];
          k++;
      }
  }
  console.log(nums);
  return k;
};