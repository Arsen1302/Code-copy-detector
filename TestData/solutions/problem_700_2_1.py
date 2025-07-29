class Solution:
def solution_700_2_1(self, A: List[List[int]]) -> int:
    row, col = len(A), len(A[0])
    
    if not A or not A[0]:
        return 0
    
    def solution_700_2_2(x,y,A):
        if 0<=x<row and 0<=y<col and A[x][y] ==1:
            A[x][y] = "T"
            solution_700_2_2(x+1,y,A)
            solution_700_2_2(x-1,y,A)
            solution_700_2_2(x,y+1,A)
            solution_700_2_2(x,y-1,A)
        
        
    for x in range(row):
        solution_700_2_2(x,0,A)
        solution_700_2_2(x,col-1,A)
    
    for y in range(1,col-1):
        solution_700_2_2(0,y,A)
        solution_700_2_2(row-1,y,A)
    
    count=0
    for x in range(row):
        for y in range(col):
            if A[x][y]==1:
                count+=1
    
    return count