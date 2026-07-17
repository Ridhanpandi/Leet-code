// Last updated: 17/07/2026, 14:45:03
1class Solution {
2public:
3    vector<vector<int>> generateMatrix(int n) {
4        vector<vector<int>> matrix(n, vector<int>(n, 0));
5        int top = 0, down = n - 1;
6        int left = 0, right = n - 1;
7        int currElement = 1;
8
9        while (currElement <= n * n) {
10            // move left to right, row = top fixed
11            for (int c = left; c <= right; c++)
12                matrix[top][c] = currElement++;
13            top++;
14
15            // move top to down, col = right fixed
16            for (int r = top; r <= down; r++)
17                matrix[r][right] = currElement++;
18            right--;
19
20            // move right to left, row = down fixed
21            for (int c = right; c >= left && currElement <= n * n; c--)
22                matrix[down][c] = currElement++;
23            down--;
24
25            // move down to top, col = left fixed
26            for (int r = down; r >= top && currElement <= n * n; r--)
27                matrix[r][left] = currElement++;
28            left++;
29        }
30
31        return matrix;
32    }
33};