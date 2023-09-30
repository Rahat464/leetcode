#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import collections
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if (board[r][c] != "." and 
                    board[r][c] in row[r] or 
                    board[r][c] in col[c] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                if board[r][c] != ".":   
                    col[c].add(board[r][c])
                    row[r].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])
            
        return True
    
# @lc code=end

