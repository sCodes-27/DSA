class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        best_buy =prices[0]
        for i in range(1,len(prices)):
            profit = prices[i]-best_buy
            max_profit = max(max_profit,profit)
            best_buy = min(best_buy,prices[i])
        return max_profit

        