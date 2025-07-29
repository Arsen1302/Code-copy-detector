class Solution:
    def solution_1390_4(self, grid: List[List[int]], x: int) -> int:
        m=len(grid)
        n=len(grid[0])
        mn=float('inf')
        numlist=[]
        for i in range(m):
            for j in range(n):
                numlist.append(grid[i][j])
        numlist.sort()
        target=numlist[m*n//2]
        res=0
        for n in numlist:
            temp=abs(n-target)
            if temp%x!=0:
                return -1
            res+=temp//x
        return res