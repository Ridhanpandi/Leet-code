# Last updated: 20/07/2026, 11:50:24
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        left = 0
4        right = len(height) - 1
5        left_max = height[left]
6        right_max = height[right]
7        water = 0
8
9        while left < right:
10            if left_max < right_max:
11                left += 1
12                left_max = max(left_max, height[left])
13                water += left_max - height[left]
14            else:
15                right -= 1
16                right_max = max(right_max, height[right])
17                water += right_max - height[right]
18        
19        return water