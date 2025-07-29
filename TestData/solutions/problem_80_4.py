class Solution:
    def solution_80_4(self, dungeon: List[List[int]]) -> int:
        m=len(dungeon)
        n=len(dungeon[0])
        
       
        #dynammic programming: dp[i][j] contains minimal health required to make it from position i,j to bottom right corner
        #only moving down or right, hence
        # if we gain=dungeon[i][j]>0 then dp[i][j]=max(1,(min(dp[i+1][j],dp[i][j+1])-gain))
        # if we damage=dungeon[i][j]<0 then dp[i][j]=-damage+min(dp[i+1][j],dp[i][j+1])
        # if nothing empty=dungeon[i][j]=0 then dp[i][j]=min(dp[i+1][j],dp[i][j+1])
        
        #no need to allocate extra storage, use dungeon to store dp values
        
        dungeon[-1][-1]=1 if dungeon[-1][-1]>=0 else 1-dungeon[-1][-1]
        
        for i in range(m-2,-1,-1):
            curr=dungeon[i][-1]
            if curr>0:
                dungeon[i][-1]=max(1,dungeon[i+1][-1]-curr)
            elif curr==0:
                dungeon[i][-1]=dungeon[i+1][-1]
            else:
                dungeon[i][-1]=-curr+dungeon[i+1][-1]
                
        for j in range(n-2,-1,-1):
            curr=dungeon[-1][j]
            if curr>0:
                dungeon[-1][j]=max(1,dungeon[-1][j+1]-curr)
            elif curr==0:
                dungeon[-1][j]=dungeon[-1][j+1]
            else:
                dungeon[-1][j]=-curr+dungeon[-1][j+1]
                
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                curr=dungeon[i][j]
                if curr>0:
                    dungeon[i][j]=max(1,(min(dungeon[i+1][j],dungeon[i][j+1])-curr))     
                elif curr==0:
                    dungeon[i][j]=min(dungeon[i+1][j],dungeon[i][j+1])     
                else:
                    dungeon[i][j]=-curr+min(dungeon[i+1][j],dungeon[i][j+1])

                    
        
        
        
        return dungeon[0][0]