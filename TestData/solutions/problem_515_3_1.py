class Solution:
    def solution_515_3_1(self, grid: List[List[int]]) -> int:
        
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def solution_515_3_2(grid,i,j,islandID):
            if i <0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1:
                return 0
            grid[i][j]=islandID
            left=solution_515_3_2(grid,i,j-1,islandID)
            right=solution_515_3_2(grid,i,j+1,islandID)
            top=solution_515_3_2(grid,i-1,j,islandID)
            bottom=solution_515_3_2(grid,i+1,j,islandID)
            return left+right+top+bottom+1
                
        

        if grid ==0 or len(grid)== 0:
            return 0
        else:
            maxx=0
            islandID=2
            m=len(grid)
            n=len(grid[0])
            mapp={}
            for i in range(0,m):
                for j in range (0,n):
                    if grid[i][j]==1:
                        size=solution_515_3_2(grid,i,j,islandID)
                        maxx=max(maxx,size)
                        mapp[islandID]=size
                        islandID+=1
                        
            
            for i in range(0,m):
                for j in range (0,n):
                    if grid[i][j]==0:
                        sett=set()
                        for direction in directions:
                            x=direction[0]+i
                            y=direction[1]+j
                            if x>-1 and y>-1 and x<m and y<n and grid[x][y]!=0:
                                sett.add(grid[x][y])
                                
                                
                        summ=1
                        for num in sett:
                            value=mapp[num]
                            summ+=value
                        maxx=max(maxx,summ)
            return maxx