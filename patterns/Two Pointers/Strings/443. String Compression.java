// https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

// Description: Given an array of characters chars, compress it using the following algorithm:
// Begin with an empty string s. For each group of consecutive repeating characters in chars:
// If the group's length is 1, append the character to s.
// Otherwise, append the character followed by the group's length.
// The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
// After you are done modifying the input array, return the new length of the array.
// You must write an algorithm that uses only constant extra space.
class Solution {

    public int compress(char[] chars) {
        int write = 0;  // Points to where to write the result in the chars array
        int read = 0;   // Points to where we are reading from in the chars array

        while (read < chars.length) {
            char currentChar = chars[read];
            int count = 0;

            // Count how many times the current character repeats consecutively
            while (read < chars.length && chars[read] == currentChar) {
                read++;
                count++;
            }

            // Write the character
            chars[write++] = currentChar;

            // If the count is greater than 1, write the count as well
            if (count > 1) {
                // Convert the count to characters and write them to the array
                for (char c : Integer.toString(count).toCharArray()) {
                    chars[write++] = c;
                }
            }
        }

        return write;  // The new length of the compressed array
    }
}


// Original thought which doesn't work because not caring for the constraint and not caring for the order 
// import java.util.HashMap;
// class Solution {
//   public int compress(char[] chars) {
//       // Step 1: Count frequencies of each character using HashMap
//       HashMap<Character, Integer> charFrequency = new HashMap<>();
//       for (char c : chars) {
//           charFrequency.put(c, charFrequency.getOrDefault(c, 0) + 1);
//       }

//       // Step 2: Write the compressed format to the array
//       int write = 0;
//       for (char c : charFrequency.keySet()) {
//           chars[write++] = c;  // Write the character
//           int count = charFrequency.get(c);
//           if (count > 1) {
//               for (char numChar : Integer.toString(count).toCharArray()) {
//                   chars[write++] = numChar;  // Write the count as a string
//               }
//           }
//       }

//       return write;  // Return the new length of the compressed array
//   }
// }
