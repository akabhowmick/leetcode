# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.


def romanToInt(self, s: str) -> int:
    # Define a dictionary to map Roman numerals to their integer values
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Initialize a variable to store the result
    result = 0
    
    # Iterate through the string from right to left
    for i in range(len(s) - 1, -1, -1):
        # Check if the current symbol is greater than the next symbol
        if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
            # If it is, subtract the current symbol's value from the result and move two indices back
            result -= roman_dict[s[i]]
        else:
            # Otherwise, add the current symbol's value to the result
            result += roman_dict[s[i]]
  
    return result