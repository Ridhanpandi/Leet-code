# Last updated: 28/08/2026, 10:36:43
1class Solution(object):
2    def subsets(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[List[int]]
6        """
7        result = []
8        
9        def backtrack(start, path):
10            result.append(list(path))
11            for i in range(start, len(nums)):
12                path.append(nums[i])
13                backtrack(i + 1, path)
14                path.pop()
15                
16        backtrack(0, [])
17        return result