class Solution:
    def solution_1689_2(self, grid: List[List[int]], k: int) -> int:
        p=10**9+7
        m=len(grid)
        n=len(grid[0])
        
        lst=[([0]*k if j else [1]+[0]*(k-1)) for j in range(n)]

        for i in range(m):
            gr=grid[i]
            klst=[0]*k
            for j in range(n):
                g=gr[j]
                l=lst[j]
                klst=[(klst[(r-g)%k]+l[(r-g)%k])%p for r in range(k)]
                lst[j]=klst

        return lst[-1][0]