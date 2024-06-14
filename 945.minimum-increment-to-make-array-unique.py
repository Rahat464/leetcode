#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#

# @lc code=start
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # Solution 1: O(n*m), O(n), where m is the average number of increments per value
        # Issue: Time Limit
        # seen = set()
        # res = 0

        # for i in range(len(nums)):
        #     while nums[i] in seen:
        #         nums[i] += 1
        #         res += 1
        #     seen.add(nums[i])
        
        # return res

        # Sol 2: O(n), O(n), by Neetcode
        res = 0
        count = [0] * (10**5 + len(nums))
        for n in nums:
            count[n] += 1
        
        for i, n in enumerate(count):
            if n > 1:
                count[i+1] += n - 1
                res += n - 1
        
        return res
        
# @lc code=end

