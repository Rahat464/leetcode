#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def fill(self, image, sr, sc, color, start_color):

        # If the current starting pixel is within bounds
        if (0 <= sr < len(image)) and (0 <= sc < len(image[sr])) and (image[sr][sc] == start_color):
            # Colour in pixel
            image[sr][sc] = color
            # Recursive call with starting pixel as current neighbour's pixel
            self.fill(image, sr+1, sc, color, start_color)
            self.fill(image, sr-1, sc, color, start_color)
            self.fill(image, sr, sc+1, color, start_color)
            self.fill(image, sr, sc-1, color, start_color)

        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # If the starting pixel is already coloured in, do nothing since it can't fill other cells.
        if image[sr][sc] == color:
            return image

        return self.fill(image, sr, sc, color, image[sr][sc])

        
# @lc code=end

