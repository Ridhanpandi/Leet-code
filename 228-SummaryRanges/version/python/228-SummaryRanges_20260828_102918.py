# Last updated: 28/08/2026, 10:29:18
1class Solution(object):
2    def moveZeroes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: None Do not return anything, modify nums in-place instead.
6        """
7        insert_pos = 0
8        
9        for i in range(len(nums)):
10            if nums[i] != 0:
11                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
12                insert_pos += 1