# Last updated: 28/08/2026, 09:44:45
1from collections import Counter
2
3
4class Solution(object):
5
6  def minWindow(self, s, t):
7    """:type s: str
8
9    :type t: str
10    :rtype: str
11    """
12    if not t or not s:
13      return ""
14
15    # Dictionary to keep track of counts of all characters in t
16    dict_t = Counter(t)
17
18    # Number of unique characters in t that need to be present in the window
19    required = len(dict_t)
20
21    # Filtered list of characters in s to skip characters not in t
22    # Stores tuples of (index, character)
23    filtered_s = []
24    for i, char in enumerate(s):
25      if char in dict_t:
26        filtered_s.append((i, char))
27
28    l, r = 0, 0
29    formed = 0
30    window_counts = {}
31
32    # (window length, left index, right index)
33    ans = float("inf"), None, None
34
35    # Look through the filtered list of characters
36    while r < len(filtered_s):
37      character = filtered_s[r][1]
38      window_counts[character] = window_counts.get(character, 0) + 1
39
40      if window_counts[character] == dict_t[character]:
41        formed += 1
42
43      # Contract the window until it ceases to be 'desirable'
44      while l <= r and formed == required:
45        character = filtered_s[l][1]
46
47        # Save the smallest window
48        end = filtered_s[r][0]
49        start = filtered_s[l][0]
50        if end - start + 1 < ans[0]:
51          ans = (end - start + 1, start, end)
52
53        window_counts[character] -= 1
54        if window_counts[character] < dict_t[character]:
55          formed -= 1
56
57        l += 1
58
59      r += 1
60
61    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]