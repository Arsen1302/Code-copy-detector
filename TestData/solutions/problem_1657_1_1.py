class Solution:
    def solution_1657_1_1(self, mat: List[List[int]], cols: int) -> int:
        n,m = len(mat),len(mat[0])
        ans = 0

        def solution_1657_1_2(state,row,rowIncludedCount):
            nonlocal ans
            if row==n:
                if sum(state)<=cols:
                    ans = max(ans,rowIncludedCount)
                return
            
            solution_1657_1_2(state[::],row+1,rowIncludedCount)
            for j in range(m):
                if mat[row][j]==1:
                    state[j] = 1
            solution_1657_1_2(state,row+1,rowIncludedCount+1)
        
        solution_1657_1_2([0]*m,0,0)
        return ans