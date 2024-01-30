#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = [] # Stack of numbers

        for t in tokens:
            if t not in "+-*/": n.append(int(t))
            else:
                op1, op2 = n.pop(), n.pop()
                if t == "+": n.append(op2 + op1)
                elif t == "-": n.append(op2 - op1)
                elif t == "*": n.append(op2 * op1)
                else: n.append(int(op2 / op1))
        
        return n.pop()
        
# @lc code=end

