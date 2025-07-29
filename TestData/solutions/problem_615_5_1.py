class Solution:
    def solution_615_5_1(self, grid: List[List[int]]) -> int:
        n=len(grid)
        
        #to print the grid current state
        #def printgrid():    
            #for i in range(n):
                #for j in range(n):
                    #print(grid[i][j],end=" ")
                #print()
            #print()
        
        # printgrid()
            
        i1=[]
        #to make a island
        def solution_615_5_2(i,j):
            #print(i,j)
            if 0<=i<n and 0<=j<n and grid[i][j]==1:
                i1.append((i,j,0))
                grid[i][j]=2
                solution_615_5_2(i+1,j)
                solution_615_5_2(i-1,j)
                solution_615_5_2(i,j+1)
                solution_615_5_2(i,j-1)
                return
            return
        
        #this finds the 1st 1 and we call the solution_615_5_2 and the island is created
        #breaker is to make sure that we only run the solution_615_5_2 function once
        breaker =False
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    solution_615_5_2(i,j)
                    breaker=True
                    break
            if breaker:
                break
                
        
        # printgrid()
        # print(i1)
        
        dir=[(1,0),(-1,0),(0,1),(0,-1)]
        
        while i1:
            i,j,d=i1.pop(0)
            # print(f"i={i} j={j} d={d}")
            #base condition for the case where we find the ans
            if grid[i][j]==1:
                return d
            for dc,dr in dir:
                p,q=dr+i,dc+j
                if 0<=p<n and 0<=q<n and grid[p][q]!=2:
                    if grid[p][q]==1:
                        return d
                    grid[p][q]=2
                    i1.append((p,q,d+1))
                    # printgrid()