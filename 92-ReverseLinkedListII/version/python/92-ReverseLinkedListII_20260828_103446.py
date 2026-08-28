# Last updated: 28/08/2026, 10:34:46
1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        """
4        :type matrix: List[List[int]]
5        :type target: int
6        :rtype: bool
7        """
8        if not matrix or not matrix[0]:
9            return False
10            
11        m, n = len(matrix), len(matrix[0])
12        left, right = 0, m * n - 1
13        
14        while left <= right:
15            mid = (left + right) // 2
16            mid_val = matrix[mid // n][mid % n]
17            
18            if mid_val == target:
19                return True
20            elif mid_val < target:
21                left = mid + 1
22            else:
23                right = mid - 1
24                
25        return False