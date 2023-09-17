#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        # Go through each string and sort it, then use that to store anagrams together in dictionary
        # where key is sorted anagram, and value is list of grouped anagrams
        for string in strs:
            anagram = "".join(sorted(string))
            if anagram not in anagrams: anagrams[anagram] = []
            anagrams[anagram].append(string)

        # Add subarrays to res
        res = []
        for val in anagrams.values():
            res.append(val)
        
        return res
        
# @lc code=end

