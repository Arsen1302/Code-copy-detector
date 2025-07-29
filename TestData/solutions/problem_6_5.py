class Solution:
    def solution_6_5(self, s: str, numRows: int) -> str:
        # rules for columns that have a diagonal
        diagcols = max(numRows-2,1) if numRows>2 else 0
        # return diagcols
        grid = [""]*numRows
        
        # while the string isn't empty
        while s:
			# insert characters 1 by 1 into each row
            for index in range(numRows):
                if s:
                    grid[index] += s[0]
                    s = s[1:]
			# insert 1 character into each appropriate designated diagonal row, starting from the bottom
            for index in range(diagcols):
                if s:
                    grid[diagcols-index] += s[0]
                    s = s[1:]
        return ''.join(grid)