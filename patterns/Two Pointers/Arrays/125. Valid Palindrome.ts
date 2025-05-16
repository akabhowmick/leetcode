// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

// Given a string s, return true if it is a palindrome, or false otherwise.

// https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

// Strings Two Pointers

 

function isPalindrome(s: string): boolean {
  // remove all non-alphanumeric characters
  const alphaRegEx = /^[a-zA-Z]+$/;
  let modifiedString = "";
  for (let i = 0; i < s.length; i++) {
    if (/^[a-zA-Z0-9]+$/.test(s[i])) {
      modifiedString += s[i].toLowerCase();
    }
  }
  console.log(modifiedString);
  // two pointer system
  let start = 0;
  let end = modifiedString.length - 1;
  while (start < end) {
    if (modifiedString[start] !== modifiedString[end]) {
      return false;
    }
    start++;
    end--;
  }
  return true;
}
