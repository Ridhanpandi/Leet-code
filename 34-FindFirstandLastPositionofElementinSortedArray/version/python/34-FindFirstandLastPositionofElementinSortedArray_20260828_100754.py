# Last updated: 28/08/2026, 10:07:54
1class Solution(object):
2    def getRow(self, rowIndex):
3        """
4        :type rowIndex: int
5        :rtype: List[int]
6        """
7        row = [1] * (rowIndex + 1)
8        
9        for i in range(2, rowIndex + 1):
10            for j in range(i - 1, 0, -1):
11                row[j] = row[j] + row[j - 1]
12                
13        return row