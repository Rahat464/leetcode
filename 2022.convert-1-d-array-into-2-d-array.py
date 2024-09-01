#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
#

# @lc code=start
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if input array can be converted
        if (m*n != len(original)): return []
        res = [[]] * m

        for row in range(0, m):
            s = row*n
            res[row] = original[s:s+n]

        return res

# @lc code=end

