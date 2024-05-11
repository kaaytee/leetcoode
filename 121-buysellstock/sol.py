class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1
        max_p = 0
        while r < len(prices):
            curr_profits = prices[r] - prices[l]
            if prices[r] >= prices[l]:
                max_p = max(curr_profits, max_p)
            else:
                l = r
            r += 1

        return max_p


# O(n) one pass through list