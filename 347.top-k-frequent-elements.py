#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [ [] for _ in range(len(nums) + 1)]
        res = []
        
        for n in nums:
            if n in freq: freq[n] += 1
            else: freq[n] = 1
        
        for key, val in freq.items():
            bucket[val].append(key)

        for i in bucket[::-1]:
            for n in i:
                res.append(n)
                if k == len(res): return res

        
# @lc code=end

