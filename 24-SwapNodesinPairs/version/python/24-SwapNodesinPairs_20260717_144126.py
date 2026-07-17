# Last updated: 17/07/2026, 14:41:26
1class Solution:
2    def findSubstring(self, s: str, words: List[str]) -> List[int]:
3        l = len(words[0])
4        d1 = {}
5        
6        for i in words:
7            if i in d1:
8                d1[i] += 1
9            else:
10                d1[i] = 1
11        ans = []
12        for start in range(l):
13            i = start
14            j = start
15            d = d1.copy()
16            while j <= len(s)-l:
17                if s[j:j+l] in d and d[s[j:j+l]] > 0:
18                    d[s[j:j+l]] -= 1
19                    j+=l
20                else:
21                    if j-i == len(words)*l:
22                        ans.append(i)
23                    while i<j and s[i:i+l] != s[j:j+l]:
24                        if s[i:i+l] in d:
25                            d[s[i:i+l]] += 1
26                        i+=l
27                    if i!=j:
28                        if s[i:i+l] in d:
29                            d[s[i:i+l]] += 1
30                        i+=l
31                    else:
32                        j+=l
33                        i = j
34            if j-i == len(words)*l:
35                ans.append(i)
36        return ans