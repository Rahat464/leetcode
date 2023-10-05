#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
        
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            i += 1 # i becomes l pointer
            r = len(nums) - 1

            # Keep looping until combination haven't been found and pointer haven't met
            while i<r:
                total = n + nums[i] + nums[r]
                if total == 0 and ([n, nums[i], nums[r]] not in res):
                    res.append([n, nums[i], nums[r]])
                else:
                    if total > 0: r -= 1
                    else: i += 1
                

        return res

# @lc code=end

