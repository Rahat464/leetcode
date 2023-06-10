#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (49.98%)
# Likes:    47234
# Dislikes: 1537
# Total Accepted:    9.8M
# Total Submissions: 19.7M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# You can return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
# 
# 
# 
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#

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
