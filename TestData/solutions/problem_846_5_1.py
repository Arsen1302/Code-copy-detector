class Solution:
    def solution_846_5_1(self, mat: List[List[int]], threshold: int) -> int:
        m,n = len(mat),len(mat[0])
        
        # 2-dimention prefix sum array
        P = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + mat[i-1][j-1]
        
        def solution_846_5_2(x1, y1, x2, y2):
            return P[x2][y2] - P[x1-1][y2] - P[x2][y1-1] + P[x1-1][y1-1]
        
        r,ans = min(m,n),0
        for i in range(1, m+1):
            for j in range(1, n+1):
                # increase the side-length of square
                for c in range(ans+1, r+1):
                    if i+c-1<=m and j+c-1<=n and solution_846_5_2(i,j,i+c-1,j+c-1)<=threshold:
                        ans += 1
                    else:
                        break
        return ans