// Last updated: 10/07/2026, 09:51:46
1class Solution {
2    public boolean isScramble(String s1, String s2) {
3        int n = s1.length();
4        boolean dp[][][] = new boolean[n + 1][n][n];
5        for (int i = 0; i < n; i++) {
6            for (int j = 0; j < n; j++) {
7                dp[1][i][j] = s1.charAt(i) == s2.charAt(j);
8            }
9        }
10        for (int length = 2; length <= n; length++) {
11            for (int i = 0; i < n + 1 - length; i++) {
12                for (int j = 0; j < n + 1 - length; j++) {
13                    for (int newLength = 1; newLength < length; newLength++) {
14                        boolean dp1[] = dp[newLength][i];
15                        boolean dp2[] = dp[length - newLength][i + newLength];
16                        dp[length][i][j] |= dp1[j] && dp2[j + newLength];
17                        dp[length][i][j] |=
18                        dp1[j + length - newLength] && dp2[j];
19                    }
20                }
21            }
22        }
23        return dp[n][0][0];
24    }
25}