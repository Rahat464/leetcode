#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert array to hashset
        consecutive = set(nums)
        # Keeps track of running length
        length = 0
        # Keeps track of longest length found
        res = 0


        # Iterate through each integer in set
        for n in nums:
            # If the previous number isn't in the array
            if (n - 1) not in consecutive:
                length = 0
                # Reset length and keep looping until consecutive integers are not in set
                while (n + length) in consecutive: length += 1

                # Update running total wth larger lengths
                res = max(length, res)
        
        return res
            
        
# @lc code=end

