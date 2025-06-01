from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0 
        right = len(s1)-1 
        s1_char_counter = Counter(s1)
        while right < len(s2):
            substr_counter = Counter(s2[left:right+1])
            if(s1_char_counter == substr_counter):
                return True
            left+=1
            right +=1
        return False 
        
        
class SolutionOptimized1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_count = Counter(s1)
        window_count = Counter()
        window_size = len(s1)
        
        # Initialize the first window
        for i in range(window_size):
            window_count[s2[i]] += 1
        
        # Check first window
        if s1_count == window_count:
            return True
        
        # Slide the window
        for i in range(window_size, len(s2)):
            # Add new character (right side of window)
            window_count[s2[i]] += 1
            
            # Remove old character (left side of window)
            left_char = s2[i - window_size]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]  # Clean up zero counts
            
            # Check if current window matches
            if s1_count == window_count:
                return True
        
        return False