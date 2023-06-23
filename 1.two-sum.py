#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # The hashmap stores numbers that have already been discovered
        # so that we can check if the number we need is already in the hashmap.
        # If so, return n and the number we need from the hashmap.
        hashmap = {}

        # Go through each number in the given array.
        # By the time we reach n, we have already checked all numbers before n.

        # We take i since there could be duplicate numbers in the array.
        # Without it, we would only get the index of the first occurence of the number.
        for i, n in enumerate(nums):
            difference = target - n
            # Check if the number we need is already in the hashmap.
            # If so. return the index of current number and the index of the number we need from the hashmap.
            if difference in hashmap: return [hashmap[difference], i]
            # If not, add the current index to the hashmap so that we can check if the number we need is in the hashmap later.
            else: hashmap[n] = i

        
# @lc code=end
