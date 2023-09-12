#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start
class Solution:
    def minDeletions(self, s: str) -> int:
        res = 0 # No of deletions required to make string good
        # Store the frequency if a letter does not occur the same no. of times as other letters
        unique = set()
        frequency = {} # Store frequency of all letters, where key is letter and val is freq

        """
        Unique and freq will have at most 26. elements and key/value pairs at most
        regardless of input size as the alphabet has 26 letters.
        Therefore the memory complexity would be O(1)
        """

        # Iterate through each letter and string and increment freq.
        for c in s:
            if c in frequency: frequency[c] += 1
            else: frequency[c] = 1

        # Iterate through values in freq and check that all values are unique
        """
        - The values are sorted in asc. order since we want to start deleting from the least common
        letter to keep deletions at its minimum
        - The time complexity of sorting would technically be O(26log26) at most,
        however since the alphabet size doesn't increase with input it will be O(1).
        """
        for val in sorted(frequency.values(), reverse=True):
            # Keep deleting values if the frequency is not unique
            while val in unique:
                val -= 1
                res += 1

            # If the value is > 0 and unique, add it to set.
            if val > 0: unique.add(val)
        
        return res
# @lc code=end

