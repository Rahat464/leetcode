#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#

# @lc code=start
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Calculate frequency: O(n) Time and space
        counts = sorted(Counter(arr).values())
        res = len(counts)

        # Remove K numbers
        for count in counts:
            if k >= count:
                k -= count
                res -= 1
            else: break

        return res

# @lc code=end

