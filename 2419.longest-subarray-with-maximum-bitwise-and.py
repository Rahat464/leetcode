#
# @lc app=leetcode id=2419 lang=python3
#
# [2419] Longest Subarray With Maximum Bitwise AND
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """ Understanding the problem:
        Find the length of the longest contigious subarray that only contains k,
        where k is the largest value in the array
        """
        
        res = 1
        k = nums[0]
        size = 1

        for i in range(1, len(nums)):
            n = nums[i]
            if (n == k and n == nums[i-1]): # Contiguous subarray continues
                size += 1
                res = max(size, res) # k not found
            elif (n == k): # Found a new potential subarray with contiguous k's
                size = 1
            elif (n>k):
                k =n
                res = 1
                size = 1

        return res
        
# @lc code=end

