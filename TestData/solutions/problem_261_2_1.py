class Solution:
	def solution_261_2_1(self, grid: List[List[int]]) -> int:
		row, col, queue = len(grid), len(grid[0]), deque()
		for x in range(row):
			for y in range(col):
				if grid[x][y] == 1:
					queue.append((x,y))
					return self.solution_261_2_2(grid, row, col, queue)

	def solution_261_2_2(self,grid, row, col, queue):
		visited = set()
		perimeter = 0
		while queue:
			x,y = queue.popleft()
			if (x,y) in visited: continue
			visited.add((x,y))
			for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
				if 0<=nx<row and 0<=ny<col:
					if grid[nx][ny] == 0:
						perimeter+=1
					if grid[nx][ny] == 1:
						queue.append((nx,ny))
				else: # if out of grid
					perimeter+=1

		return perimeter