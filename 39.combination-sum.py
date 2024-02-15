#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            
            if i >= len(candidates): return

            dfs(i + 1, subset, total)

            if total + candidates[i] <= target:
                subset.append(candidates[i])
                dfs(i, subset, total + candidates[i])
                subset.pop()

        dfs(0, [], 0)
        return res
        
# @lc code=end

