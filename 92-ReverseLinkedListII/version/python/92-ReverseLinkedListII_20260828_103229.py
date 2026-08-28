# Last updated: 28/08/2026, 10:32:29
1class Solution(object):
2    def setZeroes(self, matrix):
3        """
4        :type matrix: List[List[int]]
5        :rtype: None Do not return anything, modify matrix in-place instead.
6        """
7        m = len(matrix)
8        n = len(matrix[0])
9        is_col = False
10        
11        for i in range(m):
12            if matrix[i][0] == 0:
13                is_col = True
14            for j in range(1, n):
15                if matrix[i][j] == 0:
16                    matrix[i][0] = 0
17                    matrix[0][j] = 0
18                    
19        for i in range(1, m):
20            for j in range(1, n):
21                if matrix[i][0] == 0 or matrix[0][j] == 0:
22                    matrix[i][j] = 0
23                    
24        if matrix[0][0] == 0:
25            for j in range(n):
26                matrix[0][j] = 0
27                
28        if is_col:
29            for i in range(m):
30                matrix[i][0] = 0