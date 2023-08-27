#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Thanks neetecode for the solution
        if x < 0: return False

        # Find length of integer by checking if it's larger than 10,100,1000 etc...
        divide = 1
        while x>=10 * divide:
            divide *= 10
            
        while x:
            # r is the Least significant digit, r is the most sd
            r = x % 10
            l = x // divide

            if r!=l: return False

            # Remove the msd (e.g. 121 % 100 = 21)
            x %= divide
            # Remove the lsd (e.g. 21 // 10 = 2)
            x = x // 10

            # We divide it by 100 because we remove two digits (10*10)
            divide /= 100

        return True
# @lc code=end

