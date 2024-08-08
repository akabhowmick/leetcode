// https://leetcode.com/problems/median-of-two-sorted-arrays/
// O(n+m+log(m+n))
// two for loops then sorting then plucking out the median

class Solution {
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
      int a1 = nums1.length;
      int b1 = nums2.length;
      int[] combinedArray = new int[a1 + b1];
       for (int i = 0; i < a1; i = i + 1) {
          // Storing the elements in 
          // the resultant array
combinedArray[i] = nums1[i];
      }

      // Loop to concat the elements of second 
      // array into resultant array
      for (int i = 0; i < b1; i = i + 1) {

          // Storing the elements in the 
          // resultant array
          combinedArray[a1 + i] = nums2[i];
      }
      Arrays.sort(combinedArray);
      int arrayLength = combinedArray.length;
      if(arrayLength % 2 == 0){
          return (double)(combinedArray[(arrayLength/2 - 1)] + combinedArray[(arrayLength/2)])/2;
      } else {
          return (double)combinedArray[(arrayLength/2)];
      }
  } 
      
}