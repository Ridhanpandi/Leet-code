# Last updated: 28/08/2026, 10:27:32
1class Solution(object):
2    def containsNearbyDuplicate(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: bool
7        """
8        window = set()
9        
10        for i in range(len(nums)):
11            if nums[i] in window:
12                return True
13                
14            window.add(nums[i])
15            
16            # Maintain the window size of at most k
17            if len(window) > k:
18                window.remove(nums[i - k])
19                
20        return False