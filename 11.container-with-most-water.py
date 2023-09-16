#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = res = 0
        r = len(height) -1

        while l<r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res
        
        # Start from 0, if start/end is smaller than current index, 
        # then update unless x-difference is larger.

        # for i, n in enumerate(height):
        #     x = i-start
        #     y = min(height[start], height[end])
            
        #     if n > end-start and n > min(height[start], height[end]):
        #         start = end
        #         # end = n

        #     # Check if x will be greater than y
        #     if i-start > min(height[start], height[end]):
        #         end = i


# @lc code=end

