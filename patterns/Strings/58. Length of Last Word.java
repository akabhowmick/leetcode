
//https://leetcode.com/problems/length-of-last-word/
// Given a string s consisting of words and spaces, return the length of the last word in the string.

class Solution {
  public int lengthOfLastWord(String s) {
      String[] str = s.split(" ");
      return str[str.length - 1].length();
  }
}