#
# @lc app=leetcode id=338 lang=python3
#
# [338] counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)

        for i in range(1, n+1):
            count = 0 # counts no. of occurrences of 1
            num = i # duplicate i so that it can be modified

            # If num reaches 0, it means we have accounted for all bits
            while num != 0:
                # If num is odd, it will increment i
                count += num % 2
                # Floor division will shift bits 1 to the right
                # E.g. 14 -> 7, 7  -> 3
                # If i is odd, it will be taken care of the first time the line above is ran.
                # After that, num will be even and thus it will
                num = num//2

            ans[i] = count
        
        return ans
        
        
# @lc code=end

