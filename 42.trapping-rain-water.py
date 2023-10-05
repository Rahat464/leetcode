#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[-1]
            
        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = maxL if maxL >= height[l] else height[l]
                res += maxL - height[l]
            else:
                r -= 1
                maxR = maxR if maxR >= height[r] else height[r]
                res += maxR  - height[r]


        return res
        
# @lc code=end

