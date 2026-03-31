class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we're basically just finding the smallest sum we can find of L - R
        L = R = 0
        largestProfit = 0

        for R in range(len(prices)):
            if prices[R] - prices[L] > largestProfit: largestProfit = prices[R] - prices[L]
            if prices[R] < prices[L]: L = R
        return largestProfit