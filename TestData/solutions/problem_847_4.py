class Solution:
	def solution_847_4(self, grid: List[List[int]], k: int) -> int:
		queue=deque()
		queue.append([0,0,k,0])
		visited=set()
		steps=-1
		while queue:
			i,j,r,steps=queue.popleft()
			if (i,j,r) not in visited:
				if i-1>=0 and grid[i-1][j]!=1:
					queue.append([i-1,j,r,steps+1])
				if i-1>=0 and grid[i-1][j]==1 and r>0:
					queue.append([i-1,j,r-1,steps+1])

				if i+1<len(grid) and grid[i+1][j]!=1:
					queue.append([i+1,j,r,steps+1])
				if i+1<len(grid) and grid[i+1][j]==1 and r>0:
					queue.append([i+1,j,r-1,steps+1])

				if j-1>=0 and grid[i][j-1]!=1:
					queue.append([i,j-1,r,steps+1])
				if j-1>=0 and grid[i][j-1]==1 and r>0:
					queue.append([i,j-1,r-1,steps+1])

				if j+1<len(grid[0]) and grid[i][j+1]!=1:
					queue.append([i,j+1,r,steps+1])
				if j+1<len(grid[0]) and grid[i][j+1]==1 and r>0:
					queue.append([i,j+1,r-1,steps+1])

				if i==len(grid)-1 and j==len(grid[0])-1:
					return steps
				visited.add((i,j,r))
		return-1