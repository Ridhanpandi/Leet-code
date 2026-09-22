# Last updated: 22/09/2026, 10:13:08
1class Solution:
2    def isHappy(self, n: int) -> bool:    
3        visit = set()
4        
5        def get_next_number(n):    
6            output = 0
7            
8            while n:
9                digit = n % 10
10                output += digit ** 2
11                n = n // 10
12            
13            return output
14
15        while n not in visit:
16            visit.add(n)
17            n = get_next_number(n)
18            if n == 1:
19                return True
20        
21        return False