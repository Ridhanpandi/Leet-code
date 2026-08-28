# Last updated: 28/08/2026, 10:21:20
1class Solution(object):
2    def singleNumber(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        result = 0
8        for num in nums:
9            result ^= num
10        return result