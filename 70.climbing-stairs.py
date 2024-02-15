#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        res = [0] * n
        res[0] = 1
        res[1] = 2
        for i in range(2, n):
            res[i] += res[i-1] + res[i-2]
        
        return res[-1]
        # # Watched Neetcode's explanation of the solution (https://youtu.be/Y0lT9Fck7qI)
        # # and now attempting to write the explained solution in the video.

        # # If the number of steps is 0, 1, 2 or 3 then the ways of getting to step n is n.
        # if n<=0: return 0
        # elif n <= 3:return n

        # # Stores the number of ways of getting to step n for the next step (s1) and the one after (s2)
        # # By default, the loop will start from the 4th last step, so s1 and s2 will be 3 and 2.
        # s1, s2 = 3, 2

        # # Iterate through each step starting from the 4th last step
        # # Calculate number of combinations by adding together s1 and s2 (Fibonacci Sequence)
        # for i in range(n-4, -1, -1):
        #     temp = s1
        #     s1 += s2
        #     s2 = temp
        
        # # There is no previous step, so s1 becomes the last step.
        # return s1

        
# @lc code=end

