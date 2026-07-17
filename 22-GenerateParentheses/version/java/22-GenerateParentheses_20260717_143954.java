// Last updated: 17/07/2026, 14:39:54
1class Solution {
2    public static List<String>ans=new ArrayList<>();
3    public static void  generating( char []a,int idx,int n,int oc,int cc){
4        if(idx==n){
5                ans.add(new String(a));
6             return;
7
8        }
9
10        if(oc<n/2){
11            a[idx]='(';
12            generating(a,idx+1,n,oc+1,cc);
13
14        }
15
16        if(oc>cc){
17            a[idx]=')';
18            generating(a,idx+1,n,oc,cc+1);
19        }
20       
21    }
22    public List<String> generateParenthesis(int n) {
23        char a[]=new char[2*n];
24        ans.clear();
25        generating(a,0,2*n,0,0);
26         return ans;
27        
28    }
29}