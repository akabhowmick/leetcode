// https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75
// O(n) space and time => don't need to use the array to be honest 
// There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

// You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

class Solution {
  public int largestAltitude(int[] gain) {
      int[] altitudes = new int[(gain.length + 1)];
      for(int i = 1; i < gain.length + 1; i++){
          altitudes[i] = altitudes[i-1] + gain[i-1]; 
      }
      int answer = altitudes[0];
      for(int i = 1; i < altitudes.length; i++){
          if(altitudes[i] > answer){
              answer = altitudes[i];
          } 
      }
      return answer; 
  }
}