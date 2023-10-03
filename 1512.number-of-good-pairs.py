#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        hashmap = {}
        res = 0

        for i, n in enumerate(nums):
            if n in hashmap: hashmap[n] += 1
            else: hashmap[n] = 1
        
        for val in hashmap.values():
            res += (val * ( val - 1)) / 2
        
        return int(res)
        
# @lc code=end

