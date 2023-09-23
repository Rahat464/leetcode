#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # First index is prefiiled with 1 as it will be filled later by m
        res = [1]
        # m is used in the second iteration, where m is the product of all nums[i] visited
        m = 1

        # Multiply nums[i] with res[i], and append it to res[i+1]
        # does not iterate through nums[-1]
        # Curr res is curr num * previous res
        for i in range(0, len(nums)-1):
            res.append(nums[i]*res[i])
        
        # Second iteration, done with nums in reverse
        # Start with multiply m with current int to make postfix
        # The multiply res[i-1]'th value so that all but res[-1] is multiplied
        for i in range(len(nums) - 1, 0, -1):
            m *= nums[i]
            res[i-1] *= m
        
        return res
        
# @lc code=end

