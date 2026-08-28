# Last updated: 28/08/2026, 10:07:17
1class Solution(object):
2    def generate(self, numRows):
3        """
4        :type numRows: int
5        :rtype: List[List[int]]
6        """
7        if numRows <= 0:
8            return []
9            
10        triangle = [[1]]
11        
12        for i in range(1, numRows):
13            prev_row = triangle[-1]
14            current_row = [1]
15            
16            for j in range(1, len(prev_row)):
17                current_row.append(prev_row[j - 1] + prev_row[j])
18                
19            current_row.append(1)
20            triangle.append(current_row)
21            
22        return triangle