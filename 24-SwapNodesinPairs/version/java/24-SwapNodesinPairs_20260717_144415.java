// Last updated: 17/07/2026, 14:44:15
1class Solution {
2    public void rotate(int[][] matrix) {
3        int len=matrix.length;
4        for(int i=0;i<len;i++){
5            for(int j=i;j<len;j++){
6            int temp= matrix[i][j];
7            matrix[i][j]=matrix[j][i];
8            matrix[j][i]=temp;
9            }
10        }
11        for(int i=0;i<len;i++){
12            for(int j=0;j<len/2;j++){
13                int temp=matrix[i][j];
14                matrix[i][j]=matrix[i][len-1-j];
15                matrix[i][len-1-j]=temp;
16            }
17        }
18    }
19}