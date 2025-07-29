class Solution(object):
    def solution_1300_5_1(self, grid1, grid2):
        m=len(grid1)
        n=len(grid1[0])
        
        def solution_1300_5_2(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid2[i][j]==0:
                return 
            grid2[i][j]=0
            solution_1300_5_2(i+1,j)
            solution_1300_5_2(i-1,j)
            solution_1300_5_2(i,j+1)
            solution_1300_5_2(i,j-1)
        # here we remove the unnecesaary islands by seeing the point that if for a land in grid2 and water in grid1 it cannot be a subisland and hence island in which this land resides should be removed 
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1 and grid1[i][j]==0:
                    solution_1300_5_2(i,j)
		#now we just need to count the islands left over 			
        count=0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1:
                    
                    solution_1300_5_2(i,j)
                    count+=1
        return count 
		```