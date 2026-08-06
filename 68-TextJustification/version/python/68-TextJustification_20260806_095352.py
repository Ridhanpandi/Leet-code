# Last updated: 06/08/2026, 09:53:52
1class Solution(object):
2    def fullJustify(self, words, maxWidth):
3        """:type words: List[str]"""
4        """:type maxWidth: int"""
5        """:rtype: List[str]"""
6        res = []
7        curr_line = []
8        curr_len = 0
9
10        for word in words:
11            # If current line length + new word length + spaces between words exceeds maxWidth
12            if curr_len + len(word) + len(curr_line) > maxWidth:
13                # Format the current line
14                if len(curr_line) == 1:
15                    # If there's only one word, left-justify it with trailing spaces
16                    line = curr_line[0] + ' ' * (maxWidth - len(curr_line[0]))
17                else:
18                    # Calculate spaces needed
19                    total_spaces = maxWidth - curr_len
20                    spaces_between = len(curr_line) - 1
21                    space_slots = total_spaces // spaces_between
22                    extra_spaces = total_spaces % spaces_between
23
24                    line = ""
25                    for i in range(spaces_between):
26                        # Distribute extra spaces to the leftmost slots
27                        spaces_to_add = space_slots + (1 if i < extra_spaces else 0)
28                        line += curr_line[i] + ' ' * spaces_to_add
29                    line += curr_line[-1]  # Append the last word
30
31                res.append(line)
32                curr_line = []
33                curr_len = 0
34
35            curr_line.append(word)
36            curr_len += len(word)
37
38        # Handle the last line (left-justified)
39        last_line = ' '.join(curr_line)
40        last_line += ' ' * (maxWidth - len(last_line))
41        res.append(last_line)
42
43        return res