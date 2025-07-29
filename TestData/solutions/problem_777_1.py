class Solution:
    def solution_777_1(self, grid: List[List[int]]) -> int:
        
		# The # of rows and # of cols
        M, N, result = len(grid), len(grid[0]), -1
        
		# A list of valid points
        valid_points = {(i, j) for i in range(M) for j in range(N)}
        
		# A double-ended queue of "land" cells
        queue = collections.deque([(i, j) for i in range(M) for j in range(N) if grid[i][j] == 1])
        
        # Check if all land, or all water, an edge case
        if len(queue) == M*N or len(queue) == 0:
            return -1
        
		# BFS
        while queue:
			
			# One iteration here
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if (x, y) not in valid_points: continue
                    if grid[x][y] == 1: continue 
                    queue.append((x, y))
                    grid[x][y] = 1 # We mark water cells as land to avoid visiting them again
                    
			# Increase the iteration/result count
            result += 1
            
        return result