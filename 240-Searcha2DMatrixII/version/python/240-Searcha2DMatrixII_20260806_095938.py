# Last updated: 06/08/2026, 09:59:38
1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        """:type matrix: List[List[int]]
4        :type target: int
5        :rtype: bool
6        """
7        if not matrix or not matrix[0]:
8            return False
9        
10        m, n = len(matrix), len(matrix[0])
11        row, col = 0, n - 1
12        
13        while row < m and col >= 0:
14            current = matrix[row][col]
15            if current == target:
16                return True
17            elif current > target:
18                col -= 1
19            else:
20                row += 1
21                
22        return False
23        