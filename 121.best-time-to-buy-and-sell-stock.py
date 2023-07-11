#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Previous inefficient solution can be found on source control

        # Minimum cost is set to first day by default
        min_cost = prices[0]
        # Set to 0 so that if a larger profit is found, var is overwritten
        max_profit = 0
        
        # Iterate through prices in list
        for i, cost in enumerate(prices):
            # If the current price is greater than the minimum cost
            if min_cost < cost:
                # If the profit is greater than the current max profit
                if (cost - min_cost) > max_profit:
                    # Overwrite the profit
                    max_profit = cost - min_cost
            # If the current price is lower than the known min cost                                   
            else: min_cost = cost
        
        return max_profit
            
                
        
# @lc code=end

