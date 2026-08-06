# Last updated: 06/08/2026, 09:48:15
1class Solution:
2    def uniquePathsWithObstacles(self, obstacleGrid):
3        m = len(obstacleGrid)
4        n = len(obstacleGrid[0])
5
6        # If start or end is blocked
7        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
8            return 0
9
10        # Starting position
11        obstacleGrid[0][0] = 1
12
13        # First row
14        for j in range(1, n):
15            if obstacleGrid[0][j] == 1:
16                obstacleGrid[0][j] = 0
17            else:
18                obstacleGrid[0][j] = obstacleGrid[0][j-1]
19
20        # First column
21        for i in range(1, m):
22            if obstacleGrid[i][0] == 1:
23                obstacleGrid[i][0] = 0
24            else:
25                obstacleGrid[i][0] = obstacleGrid[i-1][0]
26
27        # Remaining cells
28        for i in range(1, m):
29            for j in range(1, n):
30                if obstacleGrid[i][j] == 1:
31                    obstacleGrid[i][j] = 0
32                else:
33                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
34
35        return obstacleGrid[m-1][n-1]