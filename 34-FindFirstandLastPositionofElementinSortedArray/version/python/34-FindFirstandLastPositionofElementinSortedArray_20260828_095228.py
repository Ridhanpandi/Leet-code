# Last updated: 28/08/2026, 09:52:28
1class Solution(object):
2    def searchRange(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        def findBound(is_first):
9            left, right = 0, len(nums) - 1
10            bound = -1
11            
12            while left <= right:
13                mid = (left + right) // 2
14                
15                if nums[mid] == target:
16                    bound = mid
17                    if is_first:
18                        right = mid - 1  # Look even further left
19                    else:
20                        left = mid + 1   # Look even further right
21                elif nums[mid] < target:
22                    left = mid + 1
23                else:
24                    right = mid - 1
25                    
26            return bound
27
28        first_pos = findBound(True)
29        last_pos = findBound(False)
30        
31        return [first_pos, last_pos]