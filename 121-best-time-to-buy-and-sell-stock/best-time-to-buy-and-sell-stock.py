class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0

        minimum = prices[0]
        maximum_profit = 0

        for price in prices[1:]:
            if price < minimum:
                minimum = price
            else:
                current_profit = price - minimum
                maximum_profit = max(maximum_profit, current_profit)

        return maximum_profit
