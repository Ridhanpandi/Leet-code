# Last updated: 28/08/2026, 10:14:33
1class Solution(object):
2    def maxProfit(self, prices):
3        """
4        :type prices: List[int]
5        :rtype: int
6        """
7        if not prices:
8            return 0
9            
10        first_buy = -prices[0]
11        first_sell = 0
12        second_buy = -prices[0]
13        second_sell = 0
14        
15        for price in prices:
16            first_buy = max(first_buy, -price)
17            first_sell = max(first_sell, first_buy + price)
18            second_buy = max(second_buy, first_sell - price)
19            second_sell = max(second_sell, second_buy + price)
20            
21        return second_sell