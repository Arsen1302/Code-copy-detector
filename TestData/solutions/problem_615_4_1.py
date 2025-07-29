class Solution:
    def solution_615_4_1(self, grid: List[List[int]]) -> int:
        n, result, queue = len(grid), 0, []
        
        def solution_615_4_2(i,j):
            queue.append((i,j))
            grid[i][j] = -1
            for x,y in [(0,-1), (0,1), (-1, 0), (1,0)]:
                xi,yj = x+i,y+j
                if 0<=xi< n and 0<=yj< n and grid[xi][yj] == 1:
                    solution_615_4_2(xi, yj)
        
        found = False
        for i in range(n):
            if found:
                break
            j = 0
            while not found and j<n:
                if grid[i][j] == 1:
                    solution_615_4_2(i,j)
                    found = True
                    break
                j+=1
        
        
        
        while queue:
            for _ in range(len(queue)):
                i,j = queue.pop(0)
                for x,y in [(0,-1), (0,1), (-1, 0), (1,0)]:
                    xi,yj = x+i,y+j
                    if 0<=xi<n and 0<=yj<n and grid[xi][yj] != -1:
                        if grid[xi][yj] == 1:
                            return result
                        elif grid[xi][yj] == 0:
                            queue.append((xi,yj))
                            grid[xi][yj] = -1
            result+=1