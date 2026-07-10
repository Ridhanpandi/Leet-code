// Last updated: 10/07/2026, 09:48:52
1class Solution {
2public:
3    int removeDuplicates(vector<int>& nums) {
4        int n = nums.size();
5
6        if (n <= 2)
7            return n;
8
9        int i = 2; // Next position to write
10
11        for (int j = 2; j < n; j++) {
12            if (nums[j] != nums[i - 2]) {
13                nums[i] = nums[j];
14                i++;
15            }
16        }
17
18        return i;
19    }
20};