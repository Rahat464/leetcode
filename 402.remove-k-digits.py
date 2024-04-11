#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        monotonic_stack = []

        for c in num:
            # Remove elements that are greater than the current element
            while k > 0 and monotonic_stack and monotonic_stack[-1] > c:
                monotonic_stack.pop()
                k -= 1
            monotonic_stack.append(c)

        # Remove the remaining elements from the stack
        del monotonic_stack[len(monotonic_stack)-k:len(monotonic_stack)]
        
        # Remove leading zeros
        return "".join(monotonic_stack).lstrip("0") or "0"
        
# @lc code=end

