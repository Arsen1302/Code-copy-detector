class Solution:
    def solution_437_1_1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        h, w = len(image), len(image[0])
        
		
        def solution_437_1_2( r, c, src_color):
            
            if r < 0 or c < 0 or r >= h or c >= w or image[r][c] == newColor or image[r][c] != src_color:
                # Reject for invalid coordination, repeated traversal, or different color
                return
            
            # update color
            image[r][c] = newColor
            
            
            # DFS to 4-connected neighbors
            solution_437_1_2( r-1, c, src_color )
            solution_437_1_2( r+1, c, src_color )
            solution_437_1_2( r, c-1, src_color )
            solution_437_1_2( r, c+1, src_color )
            
        # ---------------------------------------------------------------------------
        
        solution_437_1_2(sr, sc, src_color = image[sr][sc] )
        
        return image