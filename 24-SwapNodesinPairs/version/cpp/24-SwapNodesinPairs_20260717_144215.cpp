// Last updated: 17/07/2026, 14:42:15
1					// 😉😉😉😉Please upvote if it helps 😉😉😉😉
2class Solution {
3public:
4
5    void Sum(vector<int>& candidates, int target, vector<vector<int> >& res, vector<int>& r, int i)
6    {
7        
8        if(target == 0)
9        {
10            // if we get exact answer
11            res.push_back(r);
12            return;
13        }
14        
15        while(i <  candidates.size() && target - candidates[i] >= 0)
16        {
17            // Till every element in the array starting
18            // from i which can contribute to the target
19            r.push_back(candidates[i]);// add them to vector
20            
21            // recur for next numbers
22            Sum(candidates,target - candidates[i],res,r,i);
23            ++i;
24            
25            // Remove number from vector (backtracking)
26            r.pop_back();
27        }
28}
29    
30     
31    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
32        sort(candidates.begin(),candidates.end()); // sort candidates array
33        
34        // remove duplicates
35        candidates.erase(unique(candidates.begin(),candidates.end()),candidates.end());
36        
37        vector<int> r;
38        vector<vector<int> > res;
39        
40        Sum(candidates,target,res,r,0);
41        
42        return res;
43    }
44};