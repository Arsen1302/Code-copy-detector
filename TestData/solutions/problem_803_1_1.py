class Solution:
	def solution_803_1_1(self, grid: List[List[int]]) -> int:
		m = len(grid)
		n = len(grid[0])
		def solution_803_1_2(i,j,grid,vis,val):
			# print(i,j,grid,vis,val)
			if(i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or vis[i][j]):
				# print(i,m,j,n)
				return val
			vis[i][j] = True
			a = solution_803_1_2(i,j-1,grid,vis,val+grid[i][j])
			b = solution_803_1_2(i,j+1,grid,vis,val+grid[i][j])
			c = solution_803_1_2(i+1,j,grid,vis,val+grid[i][j])
			d = solution_803_1_2(i-1,j,grid,vis,val+grid[i][j])
			vis[i][j] = False
			return max(a,b,c,d)
		ma = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if(grid[i][j] != 0):
					vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
					ma = max(ma,solution_803_1_2(i,j,grid,vis,0))
		return ma