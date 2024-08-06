// https://leetcode.com/problems/two-sum/
// Arrays Math Random


// O(n^2) and O(n) space
class Solution {
    public int[] twoSum(int[] nums, int target) {
     
    for(int i=0;i<nums.length;i++)
     {
       for(int j=i+1;j<nums.length;j++)
        {
          if(nums[i]+nums[j]==target)
          return new int[] {i, j};
        }  
     }
       return new int [] {-1,-1};

    }

}

// O(n) time and O(n) space
class Solution {
  public int[] twoSum(int[] nums, int target) {
      Map<Integer, Integer> pairIdx = new HashMap<>();

      for (int i = 0; i < nums.length; i++) {
          int num = nums[i];
          if (pairIdx.containsKey(target - num)) {
              return new int[] { i, pairIdx.get(target - num) };
          }
          pairIdx.put(num, i);
      }

      return new int[] {};        
  }
}