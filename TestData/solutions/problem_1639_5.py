class Solution:
    def solution_1639_5(self, grid: List[List[int]]) -> List[List[int]]:
	
        n = len(grid)-2
        ans = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                ans[i][j] = max(chain(grid[i  ][j:j+3], 
                                      grid[i+1][j:j+3],
                                      grid[i+2][j:j+3]))
        
		return  ans