class Solution:
    def solution_321_3(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return
        
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        rows = len(matrix)
        cols = len(matrix[0])
        
		# Iterate through our mtrx til we find vals != 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] != 0:
				    # Use a deque for our BFS
                    q = collections.deque([])
                    q.append((row, col, 0))
                    while q:
                        r, c, dist = q.popleft()
						# When we find our first 0 we'll break and retain the dist
						# Using BFS the first 0 we come across will be the shortest dist.
                        if matrix[r][c] == 0:
                            break
						# If we are still searching for that 0.
                        if matrix[r][c] != 0:
						    # Iterate through all the possible directions we can search (up, down, l, r).
                            for dirr in directions:
							    # Create the next row, col location to inspect.
                                nr = r + dirr[0]
                                nc = c + dirr[1]
								# If the newly created point is valid (lies in our matrix bounds), append to deque.
                                if nr < rows and nr >= 0 and nc < cols and nc >= 0:
                                    q.append((nr, nc, dist + 1))
					# Update our starting location with our distance we just popped.
                    matrix[row][col] = dist
                                
        return matrix