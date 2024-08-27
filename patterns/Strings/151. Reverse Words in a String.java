// https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

// Given an input string s, reverse the order of the words.

// A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

// Return a string of the words in reverse order concatenated by a single space.

// Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

// This solution is the easy one => split 0(n) then we work with flipping and adding but it is inefficient

// tags: Strings; Two Pointers

class Solution {
  public String reverseWords(String s) {
      String[] answer = s.split(" ");
      String finalString = "";
      for(int i = answer.length-1; i >= 0; i--){
          if(!answer[i].equals("")){
              finalString+=answer[i] + " ";
          }
      }
      return finalString.strip();
  }
}

// Better solution => Two pointers 
class Solution {
    public String reverseWords(String s) {
        String[] arr = s.trim().split("\\s+");
        // This is a regular expression that matches any whitespace character, including spaces, tabs, and newlines.
        int i=0,j=arr.length-1;
        while(i<j) {
            // swapping the place values of the two pointers
            String t = arr[i];
            arr[i] = arr[j];
            arr[j] = t;
            i++;
            j--;
        }
        return String.join(" ", arr);
    }
}