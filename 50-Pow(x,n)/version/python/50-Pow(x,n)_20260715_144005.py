# Last updated: 15/07/2026, 14:40:05
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        n = len(digits)
4        
5        # Traverse the list in reverse
6        for i in range(n - 1, -1, -1):
7            if digits[i] < 9:
8                digits[i] += 1
9                return digits
10            
11            # If digit is 9, it becomes 0 and carry continues
12            digits[i] = 0
13        
14        # If we reach here, all digits were 9 (e.g., 999 -> 1000)
15        return [1] + digits