// Last updated: 22/09/2026, 10:14:53
1class Solution {
2    public String reverseVowels(String s) {
3        char[] str = s.toCharArray();
4
5        int i = 0;
6        int j = str.length - 1;
7
8        while (i < j) {
9            while (i < j && !checkVowel(str[i])) i++; 
10            while (i < j && !checkVowel(str[j])) j--;
11
12            // swap
13
14            char ch = str[i];
15            str[i++] = str[j];
16            str[j--] = ch; 
17        }
18
19        return new String(str);
20    }
21
22    public boolean checkVowel(char Char){
23        return (Char == 'a' || Char == 'A') 
24            || (Char == 'e' || Char == 'E')
25            || (Char == 'i' || Char == 'I')
26            || (Char == 'o' || Char == 'O')
27            || (Char == 'u' || Char == 'U');
28    }
29}