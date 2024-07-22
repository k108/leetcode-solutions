class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left = buy, right = sell
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            # profitable ?
            if prices[left]<prices[right]:
                profit = prices[right]-prices[left]
                max_profit = max(max_profit, profit)
            else:
                # we found a price lower then our old buy price
                left = right
            right += 1 
        
        return max_profit
        
