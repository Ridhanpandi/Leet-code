# Last updated: 28/08/2026, 10:20:35
1class Solution(object):
2    def longestConsecutive(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        num_set = set(nums)
8        longest_streak = 0
9        
10        for num in num_set:
11            if (num - 1) not in num_set:
12                current_num = num
13                current_streak = 1
14                
15                while (current_num + 1) in num_set:
16                    current_num += 1
17                    current_streak += 1
18                    
19                longest_streak = max(longest_streak, current_streak)
20                
21        return longest_streak