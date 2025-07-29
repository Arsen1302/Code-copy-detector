class Solution:
    def solution_458_4(self, N: int, mines: List[List[int]]) -> int:
        mines = {(x, y) for x, y in mines} # O(1) lookup 
        
        top = [[0]*N for _ in range(N)]
        left = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N): 
                if (i, j) in mines: continue 
                top[i][j] = 1 + top[i-1][j] if i > 0 else 1
                left[i][j] = 1 + left[i][j-1] if j > 0 else 1
        
        right = [[0]*N for _ in range(N)]
        bottom = [[0]*N for _ in range(N)]
        for i in reversed(range(N)):
            for j in reversed(range(N)): 
                if (i, j) in mines: continue 
                right[i][j] = 1 + right[i][j+1] if j+1 < N else 1
                bottom[i][j] = 1 + bottom[i+1][j] if i+1 < N else 1
        
        return max(min(top[i][j], left[i][j], right[i][j], bottom[i][j]) for i in range(N) for j in range(N))