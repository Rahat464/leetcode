#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] > 5: return False
        count = [0, 0] # 5, 10

        for bill in bills:
            if bill == 5: count[0] += 1
            elif bill == 10: 
                if count[0] > 0:
                    count[0] -= 1
                    count[1] += 1
                else: return False
                
            else:
                if count[0] >= 1  and count[1] >= 1:
                    count[0] -= 1
                    count[1] -= 1
                elif count[0] >= 3: 
                    count[0] -= 3
                else: return False
        
        return True
        
# @lc code=end