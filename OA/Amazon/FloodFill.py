from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # If starting pixel is already the target color, return original image
        if image[sr][sc] == color:
            return image
        
        # Store original color and dimensions
        original_color = image[sr][sc]
        rows, cols = len(image), len(image[0])
        
        def dfs(r: int, c: int):
            # Check if current position is valid and has original color
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                image[r][c] != original_color):
                return
            
            # Change current pixel color
            image[r][c] = color
            
            # Recursively check all 4 adjacent pixels
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left
        
        # Start DFS from the given starting position
        dfs(sr, sc)
        return image
    



