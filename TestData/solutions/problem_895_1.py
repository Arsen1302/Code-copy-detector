class Solution:
    def solution_895_1(self, grid: List[List[int]]) -> int:
        result = 0
        rows = len(grid)
        cols = len(grid[0])
        
        i = 0
        j = cols - 1
        while i < rows and j>=0:
            curr = grid[i][j]
            if(curr < 0):
                j-=1
            else:
                result+=((cols-1) - j) #capture the no.of negative number in this row and jump to next row
                i+=1
        
		#left out negative rows
        while i < rows:
            result+=cols
            i+=1
        
        return result