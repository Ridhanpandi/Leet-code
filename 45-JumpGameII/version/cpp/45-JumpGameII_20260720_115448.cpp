// Last updated: 20/07/2026, 11:54:48
1class Solution {
2public:
3    double myPow(double x, int n) {
4        bool flag=false;
5        long long m=n;
6        if(m<0){
7            m*=-1;
8            flag=true;
9        }
10        if (m == 0)
11            return 1;
12        double ot = 1;
13        while (m > 0) {
14            if (m % 2 == 0) {
15                x *= x;
16                m /= 2;
17            } else {
18                ot *= x;
19                m--;
20            }
21        }
22        if(flag){
23            return 1/ot;
24        }
25        return ot;
26    }
27};