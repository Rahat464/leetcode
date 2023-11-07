#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for opcode in operations:
          
            if opcode == "+":
                tmp = stack.pop()
                tmp1 = stack[-1] #peek

                stack.extend([tmp, tmp+tmp1])
                res += tmp + tmp1

            elif opcode == "D":
                res += stack[-1]*2
                stack.append(stack[-1]*2)

            elif opcode == "C":
                res -= stack[-1]
                del stack[-1]
            
            else:
                res += int(opcode)
                stack.append(int(opcode))
        
        return res
        
# @lc code=end

