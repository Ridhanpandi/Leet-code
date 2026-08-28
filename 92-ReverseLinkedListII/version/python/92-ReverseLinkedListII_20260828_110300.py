# Last updated: 28/08/2026, 11:03:00
1class Solution(object):
2    def largestRectangleArea(self, heights):
3        """
4        :type heights: List[int]
5        :rtype: int
6        """
7        stack = []
8        max_area = 0
9        n = len(heights)
10        
11        for i in range(n + 1):
12            current_height = heights[i] if i < n else 0
13            
14            while stack and heights[stack[-1]] > current_height:
15                h = heights[stack.pop()]
16                w = i if not stack else i - stack[-1] - 1
17                max_area = max(max_area, h * w)
18                
19            stack.append(i)
20            
21        return max_area