#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # The left pointer will point to the earliest version that is suspected to be bad
        # The right pointer will point to the latest version that is suspected to be bad
        # The true_flag will point to the latest known bad version
        l = 1
        r, true_flag = n, n

        while l<=r:
            midpoint = l + (r-l)//2

            # If the current version is bad, don't check any further versions
            if isBadVersion(midpoint) == True:
                true_flag = midpoint
                r = midpoint - 1
            else: # If the current version is good, don't check any earlier versions
                l = midpoint + 1
        
        return true_flag

# @lc code=end

