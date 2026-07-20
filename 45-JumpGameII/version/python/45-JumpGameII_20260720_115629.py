# Last updated: 20/07/2026, 11:56:29
1class Solution:
2    def spiralOrder(self, matrix):
3        res = []
4        top, bottom = 0, len(matrix) - 1
5        left, right = 0, len(matrix[0]) - 1
6
7        while top <= bottom and left <= right:
8            # Top row
9            for i in range(left, right + 1):
10                res.append(matrix[top][i])
11            top += 1
12
13            # Right column
14            for i in range(top, bottom + 1):
15                res.append(matrix[i][right])
16            right -= 1
17
18            if top <= bottom:
19                # Bottom row
20                for i in range(right, left - 1, -1):
21                    res.append(matrix[bottom][i])
22                bottom -= 1
23
24            if left <= right:
25                # Left column
26                for i in range(bottom, top - 1, -1):
27                    res.append(matrix[i][left])
28                left += 1
29
30        return res