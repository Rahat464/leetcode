#
# @lc app=leetcode id=2073 lang=python3
#
# [2073] Time Needed to Buy Tickets
#

# @lc code=start
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        for i, n in enumerate(tickets):
            # If the person comes before kth person, they buy upto tickets[k] tickets
            if i <= k: time += min(tickets[k], n)
            # If the person comes after kth person, they buy upto tickets[k]-1 tickets
            else: time += min(tickets[k]-1, n)
        
        return time
# @lc code=end

