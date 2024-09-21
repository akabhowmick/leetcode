// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

// Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

// Tags: String Sliding Window 

class Solution {
  public int maxVowels(String s, int k) {
      int maxNumberOfVowel = 0;
      String vowels = "aeiouAEIOU";  
      int currVowelCount = 0;

      // Initial vowel count 
      for (int i = 0; i < k; i++) {
          if (vowels.contains(String.valueOf(s.charAt(i)))) {
              currVowelCount++;
          }
      }
      maxNumberOfVowel = currVowelCount;

      // Sliding window
      for (int i = k; i < s.length(); i++) {
          // Remove the leftmost character of the previous window
          if (vowels.contains(String.valueOf(s.charAt(i - k)))) {
              currVowelCount--;
          }
          // Add the new character of the current window
          if (vowels.contains(String.valueOf(s.charAt(i)))) {
              currVowelCount++;
          }
          maxNumberOfVowel = Math.max(maxNumberOfVowel, currVowelCount);
      }

      return maxNumberOfVowel;
  }
}
