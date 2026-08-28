# Last updated: 28/08/2026, 10:28:18
1class Solution(object):
2    def summaryRanges(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[str]
6        """
7        result = []
8        i = 0
9        n = len(nums)
10        
11        while i < n:
12            start = nums[i]
13            
14            # Advance while numbers are consecutive
15            while i + 1 < n and nums[i + 1] == nums[i] + 1:
16                i += 1
17                
18            end = nums[i]
19            
20            # Format the range based on whether start and end are equal
21            if start == end:
22                result.append(str(start))
23            else:
24                result.append(str(start) + "->" + str(end))
25                
26            i += 1
27            
28        return result