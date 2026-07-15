# Last updated: 15/07/2026, 14:42:45
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n <= 2:
4            return n
5        
6        a, b = 1, 2
7        
8        for _ in range(3, n + 1):
9            a, b = b, a + b
10            
11        return b