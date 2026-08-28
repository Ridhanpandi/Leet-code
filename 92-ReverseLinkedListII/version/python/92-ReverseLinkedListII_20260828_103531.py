# Last updated: 28/08/2026, 10:35:31
1class Solution(object):
2    def combine(self, n, k):
3        """
4        :type n: int
5        :type k: int
6        :rtype: List[List[int]]
7        """
8        result = []
9        
10        def backtrack(start, path):
11            if len(path) == k:
12                result.append(list(path))
13                return
14            
15            # Optimization: prune branches where remaining numbers are insufficient
16            needed = k - len(path)
17            for i in range(start, n - needed + 2):
18                path.append(i)
19                backtrack(i + 1, path)
20                path.pop()
21                
22        backtrack(1, [])
23        return result