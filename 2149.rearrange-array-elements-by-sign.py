#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Three pointer solution:
        # 1. Looks at next value to be rearranged
        # 2. Looks at the next positive slot to be filled
        # 3. Looks at the next negative slot to be filled

        res = [None] * len(nums)
        positive = 0
        negative = 1

        for n in nums:
            if n > 0:
                res[positive] = n
                positive += 2
            else:
                res[negative] = n
                negative += 2

        return res
        
# @lc code=end

