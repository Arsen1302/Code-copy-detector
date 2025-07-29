class Solution:
    def solution_163_5_1(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        MOVES = [(1,0), (0,1), (-1,0), (0,-1)]
        
        @functools.cache
        def solution_163_5_2(i, j):
            path_length = 0
            for di, dj in MOVES:
                ni, nj = i+di, j+dj
                if 0<=ni<M and 0<=nj<N and matrix[ni][nj] > matrix[i][j]:
                    path_length = max(path_length, solution_163_5_2(ni, nj))
            return 1 + path_length
        
        res = 0
        for i in range(M):
            for j in range(N):
                res = max(res, solution_163_5_2(i, j))
        
        return res