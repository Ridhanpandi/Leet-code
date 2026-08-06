# Last updated: 06/08/2026, 09:52:55
1class Solution(object):
2    def minPathSum(self, grid):
3        """
4        :type grid: List[List[int]]
5        :rtype: int
6        """
7        if not grid or not grid[0]:
8            return 0
9        
10        m = len(grid)
11        n = len(grid[0])
12        
13        # Initialize the first row
14        for j in range(1, n):
15            grid[0][j] += grid[0][j - 1]
16            
17        # Initialize the first column
18        for i in range(1, m):
19            grid[i][0] += grid[i - 1][0]
20            
21        # Fill the rest of the grid
22        for i in range(1, m):
23            for j in range(1, n):
24                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
25                
26        return grid[m - 1][n - 1]