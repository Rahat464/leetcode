#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#

# @lc code=start

"""
38/38 cases passed (0 ms)
Your runtime beats 100 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (17.6 MB)
"""
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_count: int = 0

        for n in arr:
            if (n % 2 == 1): 
                odd_count += 1
                if odd_count == 3: return True
            else: odd_count = 0

        return False

# @lc code=end

