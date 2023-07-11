#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def fill(self, image, sr, sc, color, start_color):

        if (0 <= sr < len(image)) and (0 <= sc < len(image[sr])) and (image[sr][sc] == start_color):
            image[sr][sc] = color
            self.fill(image, sr+1, sc, color, start_color)
            self.fill(image, sr-1, sc, color, start_color)
            self.fill(image, sr, sc+1, color, start_color)
            self.fill(image, sr, sc-1, color, start_color)

        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:      
        
        """SOLUTION 1 - Too many recrusive calls

        # Check if starting pixel is already coloured in
        if image[sr][sc] == color: return image
        
        # Used to check which colour to fill
        start_color = image[sr][sc]
        image[sr][sc] = color

        # Vertical
        if sr > 0 and start_color == image[sr-1][sc]:
            image = self.floodFill(image, sr-1, sc, color)
        
        if (sr+1) < len(image) and start_color == image[sr+1][sc]:
            image = self.floodFill(image, sr+1, sc, color)
        
        # Horizontal
        if sc > 0 and start_color == image[sr][sc-1]:
            image = self.floodFill(image, sr, sc-1, color)
        
        if (sc+1) < len(image[sr]) and start_color == image[sr][sc+1]:
            image = self.floodFill(image, sr, sc+1, color)

        return image"""

        # SOLUTION 2

        if image[sr][sc] == color:
            return image

        return self.fill(image, sr, sc, color, image[sr][sc])   

        
# @lc code=end

