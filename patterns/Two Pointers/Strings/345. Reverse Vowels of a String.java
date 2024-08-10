class Solution {
  public String reverseVowels(String s) {
      int left = 0;
      int right = s.length() - 1;
      StringBuilder sb = new StringBuilder(s);

      while (left < right) {
          while (left < right && !isAVowel(s.charAt(left))) {
              left++;
          }
          while (left < right && !isAVowel(s.charAt(right))) {
              right--;
          }
          if (left < right) {
              char temp = s.charAt(left);
              sb.setCharAt(left, s.charAt(right));
              sb.setCharAt(right, temp);
              left++;
              right--;
          }
      }
      return sb.toString();
  }

  public boolean isAVowel(char c) {
      return "aeiouAEIOU".indexOf(c) != -1;
  }
}
