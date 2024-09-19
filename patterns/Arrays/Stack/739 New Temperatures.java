
import java.util.Stack;

// Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

// https://leetcode.com/problems/daily-temperatures/description/?envType=study-plan-v2&envId=leetcode-75

// Arrays Stack Monotonic Stack 

class Solution {
  public int[] dailyTemperatures(int[] temperatures) {
      int n = temperatures.length;
      int[] answer = new int[n]; // Initialize the result array with 0s
      Stack<Integer> stack = new Stack<>(); // Stack to store the indices of the temperatures
      
      for (int i = 0; i < n; i++) {
          // While stack is not empty and the current temperature is greater than the temperature
          // at the index stored in the stack
          while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
              int index = stack.pop(); // Pop the top of the stack
              answer[index] = i - index; // Calculate the difference in days
          }
          stack.push(i); // Push the current day index onto the stack
      }
      
      // If there are elements left in the stack, those indices will have 0 in the answer array
      // (this is already handled by the initial array of 0s)
      
      return answer;
  }
}
