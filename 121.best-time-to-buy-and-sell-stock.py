#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Inefficient solution that works for 198/211 cases
        # max_profit = 0
        # for i, cost in enumerate(prices):

        #     for revenue in prices[i:]:
        #         if (revenue - cost) > max_profit:
        #             max_profit = revenue - cost
        
        # return max_profit

        # Efficient solution
        min_cost = prices[0]
        max_profit = 0
        
        for i, cost in enumerate(prices):
            if min_cost < cost:
                if (cost - min_cost) > max_profit:
                    max_profit = cost - min_cost
                           
            else: min_cost = cost
        
        return max_profit
            
                
        
# @lc code=end

