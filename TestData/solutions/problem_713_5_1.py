class Solution:
    def solution_713_5_1(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def solution_713_5_2(mat, i, j, been, colour, center):
            if 0 <= i+1 < len(mat) and 0 <= i-1 < len(mat) and 0 <= j+1 < len(mat[i]) and 0 <= j-1 < len(mat[i]): # checking for a center
                if mat[i+1][j] == mat[i-1][j] == mat[i][j+1] == mat[i][j-1] == colour[0]:
                    center.add((i, j))
            if (i, j) not in been:
                been.add((i, j))
            if 0 <= i+1 < len(mat) and mat[i+1][j] == colour[0] and (i+1, j) not in been:
                been.add((i+1, j))
                solution_713_5_2(mat, i+1, j, been, colour, center)
            if 0 <= i-1 < len(mat) and mat[i-1][j] == colour[0] and (i-1, j) not in been:
                been.add((i-1, j))
                solution_713_5_2(mat, i-1, j, been, colour, center)
            if 0 <= j+1 < len(mat[i]) and mat[i][j+1] == colour[0] and (i, j+1) not in been:
                been.add((i, j+1))
                solution_713_5_2(mat, i, j+1, been, colour, center)
            if 0 <= j-1 < len(mat[i]) and mat[i][j-1] == colour[0] and (i, j-1) not in been:
                been.add((i, j-1))
                solution_713_5_2(mat, i, j-1, been, colour, center)


        been = set() # the surface which has to be painted
        center = set() # center of the surface
        colour = {1: -1, 0: -1} # a dictionary with the original colour and the colour which has to be used
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == row and j == col:
                    colour[0] = grid[i][j] # the original colour
                    colour[1] = color # colour to implement
                    solution_713_5_2(grid, i, j, been, colour, center)
        been = list(been)
        for i in range(len(been)):
            if been[i] not in center:
                grid[been[i][0]][been[i][1]] = colour[1]
        return grid