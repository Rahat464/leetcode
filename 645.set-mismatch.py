#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # O(n) time and space
        res = [0,0]
        visited = set()

        for n in nums:
            if n not in visited: visited.add(n)
            else: res[0] = n
        
        for n in range(1, len(nums) + 1):
            if n not in visited: res[1] = n
        
        return res
# @lc code=end

