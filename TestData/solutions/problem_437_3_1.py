class Solution:
    def solution_437_3_1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        a = image[sr][sc]
        
        def solution_437_3_2(r, c):
            nonlocal rows, cols, newColor, image
            if r < 0 or c < 0 or r>rows-1 or c>cols-1 or image[r][c]==newColor or image[r][c]!=a:
                return
            
            image[r][c] = newColor
            solution_437_3_2(r+1,c)
            solution_437_3_2(r-1,c)
            solution_437_3_2(r,c+1)
            solution_437_3_2(r,c-1)
        
        solution_437_3_2(sr, sc)
        return image