# Last updated: 28/08/2026, 11:09:40
1class Solution(object):
2    def grayCode(self, n):
3        """
4        :type n: int
5        :rtype: List[int]
6        """
7        result = [0]
8        for i in range(n):
9            for j in range(len(result) - 1, -1, -1):
10                result.append(result[j] | (1 << i))
11        return result