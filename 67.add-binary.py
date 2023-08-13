#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans, c = "", False
        len_a, len_b = len(a), len(b)
        
        for i in range(max(len_a, len_b)):
            # Convert binary at current index into int
            # If out of index, then it's equal to 0
            a_i = int(a[len_a -i-1 ]) if i < len_a else 0
            b_i = int(b[len_b -i-1 ]) if i < len_b else 0

            # Checks that if one or three are True
            # If two are true, then the output is 0 and carry should be 1.
            s = (a_i + b_i + c) % 2

            # Carry to be accounted for (2^n+1) digit addition
            # Checks that at least two are true
            c = a_i + b_i + c >= 2

            # Update answer
            ans = ("1" + ans) if s else ("0" + ans)
        
        # Account for any remaining carries
        return ("1" + ans) if c else (ans)
        
# @lc code=end

