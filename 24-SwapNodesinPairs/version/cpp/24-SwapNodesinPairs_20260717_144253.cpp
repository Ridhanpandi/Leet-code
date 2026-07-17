// Last updated: 17/07/2026, 14:42:53
1class Solution {
2public:
3    string countAndSay(int n) {
4        // base case
5        if(n==1)
6            return "1";
7        if(n==2)
8            return "11";
9        
10        // take a string equals 11
11        string str = "11";
12        
13        // now we need the value of nth term so we loop from 3 -> n
14        for(int i=3; i<=n ; i++)
15        {
16            // temp will have the ans of the next iteration i.e value of the next ith data
17            string temp = "";
18            str = str+"&"; // add a delimeter at the end
19            int cnt = 1; // counter 
20            
21            // now loop from 1st value to last value
22            for(int j = 1; j<str.length(); j++)
23            {
24                // this condition should be satisfied, if not that means new number has started occurring
25                if(str[j]!=str[j-1])
26                {
27                    temp = temp + to_string(cnt); // add the counter to temp
28                    temp = temp + str[j-1]; // add the data of the counter
29                    cnt = 1; // reset the counter to 1
30                }
31                else
32                    cnt++; // just count the freq of that number
33            }
34            
35            // after one complete traversal, make str equal to temp;
36            str = temp;
37        }
38        
39    return str;
40    }
41};