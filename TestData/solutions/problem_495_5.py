class Solution:
    def solution_495_5(self, grid: List[List[int]]) -> int:
        tp=list(zip(*grid))
        s=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                s+=min(max(grid[i]),max(tp[j]))-grid[i][j]
        return s