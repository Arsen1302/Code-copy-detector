class Solution:
	def solution_830_2_1(self, grid: List[List[int]]) -> int:
		#DFS    
		def solution_830_2_2(r,c):
			grid[r][c]=-1
			nonlocal ans
			ans+=1
			for i in range(len(grid)):
				if grid[i][c]==1:
					solution_830_2_2(i, c)

			for j in range(len(grid[0])):
				if grid[r][j]==1:
					solution_830_2_2(r, j)
		count=0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j]==1:
					ans=0
					solution_830_2_2(i,j)
					if ans>1:
						count+=ans
		return count