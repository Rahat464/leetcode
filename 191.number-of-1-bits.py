#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        # Keep looping until all bits have been shifted
        while n:
            # Increment count by 1 if n is odd
            # e.g. (3) 11 % 2 = 1
            count += n % 2
            # Shift all bits 1 to the right
            # If 0 becomes the left-most bit, count will not increment as n is even.
            # If 1 becomes left-most bit, count will increment as n is odd
            n >>= 1
        
        return count

        
# @lc code=end

