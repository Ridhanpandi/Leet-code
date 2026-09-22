// Last updated: 22/09/2026, 10:13:53
1class Solution {
2    public void reverseString(char[] s) {
3        int left = 0;
4        int right = s.length - 1;
5
6        while(left < right){
7            char temp = s[left];
8            s[left] = s[right];
9            s[right] = temp;
10
11            left++;
12            right--;
13        }
14       
15    }
16}