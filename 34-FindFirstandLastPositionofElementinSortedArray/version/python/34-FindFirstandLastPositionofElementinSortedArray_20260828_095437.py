# Last updated: 28/08/2026, 09:54:37
1class Solution(object):
2    def solveSudoku(self, board):
3        """
4        :type board: List[List[str]]
5        :rtype: None Do not return anything, modify board in-place instead.
6        """
7        rows = [set() for _ in range(9)]
8        cols = [set() for _ in range(9)]
9        boxes = [set() for _ in range(9)]
10        empty_cells = []
11
12        # Initialize the sets with pre-existing numbers on the board
13        for r in range(9):
14            for c in range(9):
15                if board[r][c] == '.':
16                    empty_cells.append((r, c))
17                else:
18                    val = board[r][c]
19                    rows[r].add(val)
20                    cols[c].add(val)
21                    box_idx = (r // 3) * 3 + (c // 3)
22                    boxes[box_idx].add(val)
23
24        def backtrack(index):
25            if index == len(empty_cells):
26                return True
27            
28            r, c = empty_cells[index]
29            box_idx = (r // 3) * 3 + (c // 3)
30            
31            for val in '123456789':
32                if val not in rows[r] and val not in cols[c] and val not in boxes[box_idx]:
33                    # Make choice
34                    board[r][c] = val
35                    rows[r].add(val)
36                    cols[c].add(val)
37                    boxes[box_idx].add(val)
38                    
39                    if backtrack(index + 1):
40                        return True
41                    
42                    # Undo choice (backtrack)
43                    board[r][c] = '.'
44                    rows[r].remove(val)
45                    cols[c].remove(val)
46                    boxes[box_idx].remove(val)
47                    
48            return False
49
50        backtrack(0)