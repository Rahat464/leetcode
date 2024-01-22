#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique = set()
        freq = {}

        for n in arr:
            if n not in freq: freq[n] = 1
            else: freq[n] += 1
        
        for val in freq.values():
            if val not in unique: unique.add(val)
            else: return False
        
        return True

        
# @lc code=end

