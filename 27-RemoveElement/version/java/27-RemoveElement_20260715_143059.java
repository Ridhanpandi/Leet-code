// Last updated: 15/07/2026, 14:30:59
1class Solution {
2    public int removeElement(int[] nums, int val) {
3        int k = 0;
4
5        for (int i = 0; i < nums.length; i++) {
6            if (nums[i] != val) {
7                nums[k] = nums[i];
8                k++;
9            }
10        }
11
12        return k;        
13    }
14}