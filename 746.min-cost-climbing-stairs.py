#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        
        return min(cost[-1], cost[-2])

        # ORIGINAL SOLUTION
        # cost.append(0)

        # for i in range(len(cost) - 3, -1, -1):
        #     cost[i] += min(cost[i + 1], cost[i + 2])

        # return cost[0] if cost[0] < cost[1] else cost[1]
        
# @lc code=end

