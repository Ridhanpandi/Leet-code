# Last updated: 28/08/2026, 09:56:02
1class Solution(object):
2    def subsetsWithDup(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[List[int]]
6        """
7        nums.sort()
8        result = []
9        
10        def backtrack(start, path):
11            result.append(list(path))
12            
13            for i in range(start, len(nums)):
14                # If it's a duplicate and not the first time we see it at this level, skip
15                if i > start and nums[i] == nums[i - 1]:
16                    continue
17                
18                path.append(nums[i])
19                backtrack(i + 1, path)
20                path.pop()
21                
22        backtrack(0, [])
23        return result