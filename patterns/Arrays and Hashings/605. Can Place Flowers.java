// https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
// You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
// Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
// O(n) runtime O(1) space 
// Tags Array 

class Solution {
  public boolean canPlaceFlowers(int[] flowerbed, int n) {
      for(int i = 0; i < flowerbed.length; i++){
          if(n==0){
              break; 
          }
          if(flowerbed[i] == 1){
              //skipping one 
              i++; 
          } else {
              if((i+1 <flowerbed.length && (flowerbed[i+1] != 1))||(i == flowerbed.length - 1)){
                  n--;
                  i++;
              } 
          }
      }
      return n == 0; 
  }
}

