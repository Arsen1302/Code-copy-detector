class Solution:
    def solution_89_5_1(self, grid: List[List[str]]) -> int:
        count = 0
        R, C = len(grid), len(grid[0])
        
        
        def solution_89_5_2(r, c):
            grid[r][c] = '0'
            if r-1 >= 0 and grid[r-1][c] == '1':
                solution_89_5_2(r-1, c)
            if r+1 < R and grid[r+1][c] == '1':
                solution_89_5_2(r+1, c)
            if c+1 < C and grid[r][c+1] == '1':
                solution_89_5_2(r, c+1)
            if c-1 >= 0 and grid[r][c-1] == '1':
                solution_89_5_2(r, c-1)
                
                
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    solution_89_5_2(row, col)
                    
        return count
        
# first we find the 1 valued element using two for loops and then we update their values to 0 so 
# that when we backtrack (like r-1) then it will not keep on running and when values of all of it's connected
# elements become 0, we come out of the solution_89_5_2(). This keeps on happening as the 2 for loops continue finding the '1' valued element.