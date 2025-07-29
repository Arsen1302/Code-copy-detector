class Solution:
    def solution_458_1(self, N: int, mines: List[List[int]]) -> int:
        mat = [[1]*N for _ in range(N)]
        for x, y in mines: mat[x][y] = 0                   # create matrix with mine
            
        up = [[0]*N for _ in range(N)]                     # count 1s above mat[i][j] if mat[i][j] is 1
        for i in range(N):
            for j in range(N):
                if mat[i][j]: 
                    up[i][j] = 1
                    if i > 0: up[i][j] += up[i-1][j] 
                
        down = [[0]*N for _ in range(N)]                   # count 1s below mat[i][j] if mat[i][j] is 1
        for i in range(N-1, -1, -1):
            for j in range(N):
                if mat[i][j]: 
                    down[i][j] = 1
                    if i < N-1: down[i][j] += down[i+1][j] 
                    
        left = [[0]*N for _ in range(N)]                   # count 1s on the left side of mat[i][j] if mat[i][j] is 1
        for i in range(N):
            for j in range(N):
                if mat[i][j]:
                    left[i][j] = 1
                    if j > 0: left[i][j] += left[i][j-1]
                    
        right = [[0]*N for _ in range(N)]                  # count 1s on the right side of mat[i][j] if mat[i][j] is 1
        for i in range(N):
            for j in range(N-1, -1, -1):
                if mat[i][j]:
                    right[i][j] = 1
                    if j < N-1: right[i][j] += right[i][j+1]
         
		# find the largest + sign by using cached directions information
        return max(min([up[i][j], down[i][j], left[i][j], right[i][j]]) for i in range(N) for j in range(N))