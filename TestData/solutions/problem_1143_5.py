class Solution:
    
    def solution_1143_5(self, stones: List[int]) -> int:
        n = len(stones)
        df = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-2,-1,-1):
            s=stones[i]
            for j in range(i+1,n):
                s+=stones[j]
                df[i][j] = max(s-stones[i]-df[i+1][j],s-stones[j]-df[i][j-1])   
        return df[0][n-1]