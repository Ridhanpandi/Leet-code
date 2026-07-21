# Last updated: 21/07/2026, 08:58:43
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        maxSum = float('-inf')
4        currentSum = 0
5        
6        for num in nums:
7            currentSum += num
8            
9            if currentSum > maxSum:
10                maxSum = currentSum
11            
12            if currentSum < 0:
13                currentSum = 0
14        
15        return maxSum