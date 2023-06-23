#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # This stack will keep track of open parentheses
        stack = []
        # Hashmap stores the closing parentheses of each type
        match = {"(" : ")", "[" : "]", "{" : "}"}

        # Iterate through each character
        for bracket in s:
            # Check if the character is an open bracket by checking if it's a key in the hashmap
            # If it's an open bracket, append to the stack
            if bracket in match.keys(): stack.append(bracket)
            # If not, check the stack for the most recent opened bracket.
            else:
                # Peek top item in stack and check that the closing bracket matches.
                # Also check that stack is not empty
                if stack and match[stack[-1]] == bracket:
                    stack.pop()
                # If it does not match, it means that it is not a matching bracket
                else: return False
        
        # If there was a mismatching bracket, it would've returned false by now
        return True if not stack else False

# @lc code=end

