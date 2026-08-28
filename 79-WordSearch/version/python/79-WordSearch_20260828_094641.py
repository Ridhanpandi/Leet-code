# Last updated: 28/08/2026, 09:46:41
1class Solution(object):
2    def exist(self, board, word):
3        """
4        :type board: List[List[str]]
5        :type word: str
6        :rtype: bool
7        """
8        rows, cols = len(board), len(board[0])
9        
10        def dfs(r, c, i):
11            # If we matched all characters in the word
12            if i == len(word):
13                return True
14            
15            # Check bounds and character match
16            if (r < 0 or c < 0 or 
17                r >= rows or c >= cols or 
18                board[r][c] != word[i]):
19                return False
20            
21            # Temporarily mark the cell as visited
22            temp = board[r][c]
23            board[r][c] = '#'
24            
25            # Explore all 4 adjacent directions
26            found = (dfs(r + 1, c, i + 1) or 
27                     dfs(r - 1, c, i + 1) or 
28                     dfs(r, c + 1, i + 1) or 
29                     dfs(r, c - 1, i + 1))
30            
31            # Backtrack: restore the cell's original value
32            board[r][c] = temp
33            
34            return found
35
36        # Iterate through every cell to find a starting point
37        for r in range(rows):
38            for c in range(cols):
39                if board[r][c] == word[0] and dfs(r, c, 0):
40                    return True
41                    
42        return False