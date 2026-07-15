# Last updated: 15/07/2026, 14:41:21
1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        res = []
4        i, j = len(a) - 1, len(b) - 1
5        carry = 0
6        
7        while i >= 0 or j >= 0 or carry:
8            total = carry
9            if i >= 0:
10                total += int(a[i])
11                i -= 1
12            if j >= 0:
13                total += int(b[j])
14                j -= 1
15            
16            res.append(str(total % 2))
17            carry = total // 2
18            
19        return "".join(reversed(res))