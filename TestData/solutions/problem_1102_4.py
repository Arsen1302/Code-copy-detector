class Solution:
    def solution_1102_4(self, grid: List[List[int]]) -> int:
        # Base case
        if len(grid)==1 and len(grid[0])==1:
            return 0
        
        row , col = len(grid) , len(grid[0])
        visited = set()  # set : store indices (i,j) which we have visited already before reaching destination
        
        hp = [] # Min heap
        
        visited.add((0,0))
        i,j = 0,0  # statrt point
 
        ans = 0
        
        # while current not equal to destination keep traverse the grid 
        while (i,j) != (row-1,col-1):
            # down
            if i+1<row and (i+1,j) not in visited:
                d = abs(grid[i][j]-grid[i+1][j])
                heapq.heappush(hp,[d,i+1,j])
            
            # up
            if i-1>=0 and (i-1,j) not in visited:
                d = abs(grid[i][j]-grid[i-1][j])
                heapq.heappush(hp,[d,i-1,j])
            
            # right
            if j+1<col and (i,j+1) not in visited:
                d = abs(grid[i][j+1]-grid[i][j])
                heapq.heappush(hp,[d,i,j+1])
            
            # left
            if j-1>=0 and (i,j-1) not in visited:
                d = abs(grid[i][j-1]-grid[i][j])
                heapq.heappush(hp,[d,i,j-1])
            
            # top of heap tells us that what is minimum path effort we should take next
            d,p,q = heapq.heappop(hp)

            ans = max(ans,d) 
            visited.add((p,q))
            
            # change current point
            i,j = p,q 
            
        return ans