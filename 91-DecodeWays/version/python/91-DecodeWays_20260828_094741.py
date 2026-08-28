# Last updated: 28/08/2026, 09:47:41
1class Solution(object):
2    def numDecodings(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        if not s or s[0] == '0':
8            return 0
9            
10        n = len(s)
11        # prev2 represents dp[i-2], prev1 represents dp[i-1]
12        prev2 = 1
13        prev1 = 1
14        
15        for i in range(1, n):
16            current = 0
17            
18            # Single digit decode (1-9)
19            if s[i] != '0':
20                current += prev1
21                
22            # Two digit decode (10-26)
23            two_digit = int(s[i-1:i+1])
24            if 10 <= two_digit <= 26:
25                current += prev2
26                
27            prev2 = prev1
28            prev1 = current
29            
30        return prev1