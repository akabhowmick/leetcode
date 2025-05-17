// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

// Topics: Arrays Two-Pointers

function strStr(haystack: string, needle: string): number {
  if (needle === "") return 0;
  if (haystack.length < needle.length) return -1;

  for (let i = 0; i <= haystack.length - needle.length; i++) {
      let j = 0;
      while (j < needle.length && haystack[i + j] === needle[j]) {
          j++;
      } // only need to update j inside the while loop because as j increases so does i+j 
      if (j === needle.length) {
          return i;
      }
  }
  return -1;
}
