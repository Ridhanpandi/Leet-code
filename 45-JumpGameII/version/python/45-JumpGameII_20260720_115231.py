# Last updated: 20/07/2026, 11:52:31
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        near = far = jumps = 0
4
5        while far < len(nums) - 1:
6            farthest = 0
7            for i in range(near, far + 1):
8                farthest = max(farthest, i + nums[i])
9            
10            near = far + 1
11            far = farthest
12            jumps += 1
13        
14        return jumps