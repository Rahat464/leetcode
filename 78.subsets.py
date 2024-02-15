#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # SOLUTION FROM NEETCODE.IO

        # Basically, for every integer we can decide whether to include or not to include it
        # Traversing left means we include and traversing right means we don't include
        # Hence when traversing left, we append to the list
        # When traversing right, we pop it from the list to exclude the subset from the final answer

        res = []
        subset = []
        def dfs(i):
            # If we've already gone through all numbers, add the entire list to the array
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Don' include
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
        
# @lc code=end

