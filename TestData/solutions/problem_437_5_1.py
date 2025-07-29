class Solution:
    def solution_437_5_1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        startingColor = image[sr][sc]
        
        visited = [[0 for x in range(col)] for y in range(row)]
        
        def solution_437_5_2(i, j):
            # if the current node is not of the starting color
            # or is not a valid cell, return, we don't have work here
            if i < 0 or i > row - 1 or j < 0 or j > col - 1 or image[i][j] != startingColor:
                return
            
            # return if current node is visited
            # mark it as visited otherwise
            if visited[i][j]:
                return
            visited[i][j] = 1
            
            # update the color on this node
            image[i][j] = newColor
            
            # recursively try all adjacent cells of the current node
            return solution_437_5_2(i-1, j) or solution_437_5_2(i+1, j) or solution_437_5_2(i, j-1) or solution_437_5_2(i, j+1)
        
        solution_437_5_2(sr, sc)
        return image