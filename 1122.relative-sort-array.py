#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}
        for n in arr2:
            freq[n] = 0

        # Scan through arr1, counting the values found in arr2
        extra = []
        for n in arr1:
            if n in freq: freq[n] += 1
            else: extra.append(n)
        

        # Go through hashmap, rebuilding arr1
        ptr = 0
        for n in arr2:
            while freq[n] > 0:
                arr1[ptr] = n
                freq[n] -= 1
                ptr += 1
        

        # Combine the two arrays
        return arr1[:ptr] + sorted(extra)
# @lc code=end

