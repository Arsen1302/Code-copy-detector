class Solution:
    def solution_983_4_1(self, grid: List[List[int]]) -> int:
        @cache
        def solution_983_4_2(row,r1,r2):
            if row < len(grid) and 0 <= r1 < r2 < len(grid[0]):
                return grid[row][r1]+grid[row][r2]+ max(solution_983_4_2(row+1,r1+d1,r2+d2) for d1,d2 in itertools.product((-1,0,1),(-1,0,1)))
            return 0
        return solution_983_4_2(0,0,len(grid[0])-1)