1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        profit = 0
4
5        min_price = prices[0]
6
7        for p in prices[1:]:
8            if p < min_price:
9                min_price = p
10
11            profit = max(profit, p - min_price)
12
13        return profit
14