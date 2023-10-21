#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        # Iterate through each character and solve by tacking one bracket at a time
        for c in s:
            # If a closing bracket is found, it means there must be an opening bracket
            # Hence, keep popping until the contents of the brackets have been decoded
            if ']' == c:
                # tmp stores current string being decoded
                tmp = ""
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                
                # Remove [
                stack.pop()

                # Find k
                n = ""
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                
                stack.append( (int(n) * tmp) )
            
            # Keep adding to stack if a closing bracket hasn't been found
            else: stack.append(c)       

        res = ""
        for c in stack: res += c
        
        return res
                
# @lc code=end

