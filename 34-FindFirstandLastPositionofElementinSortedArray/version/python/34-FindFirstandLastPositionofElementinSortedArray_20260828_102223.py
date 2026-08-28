# Last updated: 28/08/2026, 10:22:23
1class Solution(object):
2    def wordBreak(self, s, wordDict):
3        """
4        :type s: str
5        :type wordDict: List[str]
6        :rtype: bool
7        """
8        word_set = set(wordDict)
9        n = len(s)
10        dp = [False] * (n + 1)
11        dp[0] = True
12        
13        for i in range(1, n + 1):
14            for j in range(i):
15                if dp[j] and s[j:i] in word_set:
16                    dp[i] = True
17                    break
18                    
19        return dp[n]