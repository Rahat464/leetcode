#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """
        167/167 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 41.65 % of python3 submissions (18.1 MB)
        """
        pos: int = 0
        neg: int = 0

        for n in nums:
            if n > 0: pos += 1
            elif n < 0: neg += 1

        return max(pos, neg)
# @lc code=end

