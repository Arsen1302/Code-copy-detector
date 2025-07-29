class Solution:
def solution_700_1_1(self, A: List[List[int]]) -> int:
    row, col = len(A), len(A[0])
    
    if not A or not A[0]:
        return 0
    
    boundary1 = deque([(i,0) for i in range(row) if A[i][0]==1]) + deque([(i,col-1) for i in range(row) if A[i][col-1]==1])
    boundary2 = deque([(0,i) for i in range(1,col-1) if A[0][i]==1]) + deque([(row-1,i) for i in range(1,col-1) if A[row-1][i]==1])
        
    queue = boundary1+boundary2
    
    
    def solution_700_1_2(queue,A):
        visited = set()
        while queue:
            x,y = queue.popleft()
            A[x][y] = "T"
            if (x,y) in visited: continue
            visited.add((x,y))
            for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0<=nx<row and 0<=ny<col and A[nx][ny]==1:
                    A[nx][ny] = "T"
                    queue.append((nx,ny))
        return A
    
    solution_700_1_2(queue,A)
    
    count = 0
    for x in range(row):
        for y in range(col):
            if A[x][y] == 1:
                count+=1
    return count