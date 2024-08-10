//https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
// Tags: Two_Pointers String
// Description: You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

class Solution {
  public String mergeAlternately(String word1, String word2) {
      int stringLength = word1.length() + word2.length(); 
      int w1Pointer = 0; 
      int w2Pointer = 0; 
      String answer = ""; 

      while (w1Pointer < word1.length() && w2Pointer < word2.length()) {
          // Alternating between word1 and word2 characters
          if (w1Pointer < word1.length()) {
              answer += word1.charAt(w1Pointer);
              w1Pointer++;
          }

          if (w2Pointer < word2.length()) {
              answer += word2.charAt(w2Pointer);
              w2Pointer++;
          }
      }

      // Append the remaining characters from either word1 or word2
      if (w1Pointer < word1.length()) {
          answer += word1.substring(w1Pointer);
      } else if (w2Pointer < word2.length()) {
          answer += word2.substring(w2Pointer);
      }

      return answer; 
  }
}
