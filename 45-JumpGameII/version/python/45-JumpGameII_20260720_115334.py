# Last updated: 20/07/2026, 11:53:34
1class Solution:
2    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
3        ans = []
4        perm = []
5        pick = [False]*len(nums)
6        nums.sort()
7
8        def backtrack():
9            if len(perm) == len(nums):
10                if perm.copy() not in ans: 
11                    ans.append(perm.copy())
12                    return 
13            
14            for i in range(len(nums)):
15                if not pick[i]:
16                    perm.append(nums[i])
17                    pick[i] = True
18                    backtrack()
19
20                    perm.pop()
21                    pick[i] = False
22        backtrack()
23        
24        return ans