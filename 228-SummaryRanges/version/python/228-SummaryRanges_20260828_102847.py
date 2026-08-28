# Last updated: 28/08/2026, 10:28:47
1class Solution(object):
2    def hIndex(self, citations):
3        """
4        :type citations: List[int]
5        :rtype: int
6        """
7        n = len(citations)
8        left, right = 0, n - 1
9        h_index = 0
10        
11        while left <= right:
12            mid = (left + right) // 2
13            papers_count = n - mid
14            
15            if citations[mid] >= papers_count:
16                h_index = papers_count
17                right = mid - 1  # Try to find a larger h-index on the left
18            else:
19                left = mid + 1
20                
21        return h_index