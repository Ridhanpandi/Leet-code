# Last updated: 15/07/2026, 14:38:13
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        m, n = len(word1), len(word2)
4        # Create a (m+1) x (n+1) DP table
5        dp = [[0] * (n + 1) for _ in range(m + 1)]
6        
7        # Initialize base cases
8        for i in range(m + 1): dp[i][0] = i
9        for j in range(n + 1): dp[0][j] = j
10            
11        for i in range(1, m + 1):
12            for j in range(1, n + 1):
13                if word1[i-1] == word2[j-1]:
14                    dp[i][j] = dp[i-1][j-1]
15                else:
16                    dp[i][j] = 1 + min(dp[i-1][j],    # Delete
17                                       dp[i][j-1],    # Insert
18                                       dp[i-1][j-1])  # Replace
19        return dp[m][n]