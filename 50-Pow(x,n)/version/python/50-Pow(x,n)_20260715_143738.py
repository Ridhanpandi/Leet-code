# Last updated: 15/07/2026, 14:37:38
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        stack = []
4        # Split by '/' and iterate through components
5        for part in path.split('/'):
6            if part == '..':
7                if stack:
8                    stack.pop()
9            elif part and part != '.':
10                stack.append(part)
11        
12        # Join components with '/' and ensure it starts with '/'
13        return "/" + "/".join(stack)