class Solution:
    def solution_437_2_1(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        start_color = image[sr][sc]
        
        def solution_437_2_2(x, y):
            if x < 0 or x >= len(image): return
            if y < 0 or y >= len(image[0]): return
            
            if image[x][y] == color: return
            if image[x][y] != start_color: return
            
            image[x][y] = color
            
            solution_437_2_2(x-1, y)
            solution_437_2_2(x+1, y)
            solution_437_2_2(x, y+1)
            solution_437_2_2(x, y-1)
        
        solution_437_2_2(sr, sc)
        return image