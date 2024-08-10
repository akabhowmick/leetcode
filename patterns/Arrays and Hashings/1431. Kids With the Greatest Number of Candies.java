// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

// There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

// Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

// Note that multiple kids can have the greatest number of candies.

// O(n) runtime and space 

class Solution {
  public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
      List<Boolean> answer = new ArrayList<Boolean>(); 
      int currentMax = 0; 
      //find the currentMax
      for(int i = 0; i < candies.length; i++ ){
          if(candies[i] >= currentMax){
              currentMax = candies[i];
          }
      }

      //check that after adding the extra candies each kid has the most
      for(int i = 0; i < candies.length; i++ ){
          if(candies[i]+extraCandies >= currentMax){
              answer.add(true);
          } else {
              answer.add(false);
          }
      }
      return answer; 
  }
}