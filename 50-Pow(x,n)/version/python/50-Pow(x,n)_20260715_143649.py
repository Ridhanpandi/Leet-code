# Last updated: 15/07/2026, 14:36:49
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        # Handle negative exponent
4        if n < 0:
5            x = 1 / x
6            n = -n
7        
8        result = 1
9        current_product = x
10        
11        # Iterative Binary Exponentiation
12        while n > 0:
13            # If n is odd, multiply the result by current_product
14            if n % 2 == 1:
15                result *= current_product
16            
17            # Square the base and divide n by 2
18            current_product *= current_product
19            n //= 2
20            
21        return result