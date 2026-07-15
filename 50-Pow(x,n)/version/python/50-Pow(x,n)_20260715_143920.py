# Last updated: 15/07/2026, 14:39:20
1class Solution:
2    def isNumber(self, s: str) -> bool:
3        seen_digit = seen_dot = seen_exponent = False
4        
5        for i, char in enumerate(s):
6            if char.isdigit():
7                seen_digit = True
8            elif char in ["+", "-"]:
9                # Sign is only valid at start or after 'e'/'E'
10                if i > 0 and s[i-1] not in ["e", "E"]:
11                    return False
12            elif char == ".":
13                # Dot is only valid if no dot or exponent seen yet
14                if seen_dot or seen_exponent:
15                    return False
16                seen_dot = True
17            elif char in ["e", "E"]:
18                # Exponent is valid if digit seen and no exponent seen yet
19                if seen_exponent or not seen_digit:
20                    return False
21                seen_exponent = True
22                seen_digit = False # Must see another digit after 'e'
23            else:
24                return False
25        
26        return seen_digit