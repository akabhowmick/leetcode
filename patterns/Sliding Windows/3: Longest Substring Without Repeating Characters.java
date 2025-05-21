// https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
// Difficulty: Medium
// tags: sliding window variable

// Problem
/*
Given a string s, find the length of the longest substring without repeating characters.
*/

// Solution
// O(n) time and O(1) space. The space is constant since it holds at most one instance of any possible english character.  We create a set that will track the current characters in the window, and two pointers starting at the beginning. As soon as we reach a new character, check if it is in the set. If it isn't, get a new size and increment r. If it is, we need to start decrementing from the left until we remove that characters. For instance "abcsdefsg". When we hit the second s, we need to decrement from the left until the left reaches right past the initial s. As we decrement, remove those characters from the set. We only need to remove it once since the window cannot contain two of the same character (otherwise we would've moved the window)

import java.util.Set;


class Solution {
  public int lengthOfLongestSubstring(String s) {
    int leftPointer = 0; 
    int rightPointer = 0;
    HashSet<Character> hash_Set = new HashSet<Character>();
    int longestSubString = 0; 
    while(rightPointer < s.length()){
      char current = s.charAt(leftPointer); 
      // if never seen before
      if(!hash_Set.contains(current)){
        hash_Set.add(current);
        longestSubString = Math.max(longestSubString, rightPointer - leftPointer + 1);
        System.out.println(longestSubString);
      }// if already seen
      else{
        while(s.charAt(leftPointer)!= current){
          hash_Set.remove(s.charAt(leftPointer));
          leftPointer++;
        }
        leftPointer++;
      } 
      rightPointer++;
      System.out.println(longestSubString);
    }
    return longestSubString; 
  }
}