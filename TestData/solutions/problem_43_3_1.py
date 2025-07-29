class Solution:
def solution_43_3_1(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    def solution_43_3_2(i,j):
        if i<0 or i>=m or j<0 or j>=n or board[i][j]!='O':
            return
        
        board[i][j]="*"
        solution_43_3_2(i+1,j)
        solution_43_3_2(i-1,j)
        solution_43_3_2(i,j+1)
        solution_43_3_2(i,j-1)
          
    m=len(board)
    n=len(board[0])
    if m<3 or n<3:
        return
    
    for i in range(m):
        solution_43_3_2(i,0)
        solution_43_3_2(i,n-1)
    
    for j in range(n):
        solution_43_3_2(0,j)
        solution_43_3_2(m-1,j)
    
    for i in range(m):
        for j in range(n):
            if board[i][j]=="*":
                board[i][j]="O"
            elif board[i][j]=="O":
                board[i][j]="X"      
    return