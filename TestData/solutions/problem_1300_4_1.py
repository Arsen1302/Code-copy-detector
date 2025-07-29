class Solution:
    def solution_1300_4_1(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # Time complexity: O(m*n+m*n)=>O(m*n) (we are iteraing twice through every cell)
        # Space complexity: O(1)
        
        m=len(grid2)
        n=len(grid2[0])
        
        def solution_1300_4_2(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid2[i][j]==0:return 
			# update the value as we don't want to navigate the same cell again
            grid2[i][j]=0
            #visit all directions
            solution_1300_4_2(i,j-1)
            solution_1300_4_2(i,j+1)
            solution_1300_4_2(i-1,j)
            solution_1300_4_2(i+1,j)
        
        for i in range(m):
            for j in range(n):
                #removing potenial islands which are not present in grid1
                if grid2[i][j]==1 and grid1[i][j]==0:
                    solution_1300_4_2(i,j)
        count=0
        for i in range(m):
            for j in range(n):
                #simply calculating different islands
                if grid2[i][j]==1:
                    count+=1
                    solution_1300_4_2(i,j)
        return count