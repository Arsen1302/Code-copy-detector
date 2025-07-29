class Solution:
    def solution_142_3_1(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        life = []
        for i in range(len(board)):
            col = []
            for j in range(len(board[0])):
                col.append(board[i][j])
            life.append(col)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    if self.solution_142_3_2(board,i,j) == True:
                        life[i][j] = 0
                else:
                    if self.solution_142_3_2(board,i,j) == True:
                        life[i][j] = 1
        for i in range(len(life)):
            for j in range(len(life[0])):
                board[i][j] = life[i][j]
                
    def solution_142_3_2(self,board,i,j):
        count = 0
        if board[i][j]==1:
            #diagonal top left to bottom right
            if i !=0 and j !=0 :
                if board[i-1][j-1] == 1:
                    count+=1
            if i != len(board)-1 and j != len(board[0])-1:
                if board[i+1][j+1] == 1:
                    count+=1
            #diagonal top right to bottom left
            if i!=0 and j != len(board[0])-1:
                if board[i-1][j+1] ==1:
                    count+=1
            if i!= len(board)-1 and j!=0:
                if board[i+1][j-1] == 1:
                    count +=1
            #top and bottom vertically
            if i!=0 and board[i-1][j]==1:
                count+=1
            if i!= len(board)-1 and board[i+1][j]==1:
                count +=1
            #left and right horizontally
            if j!=0 and board[i][j-1] ==1:
                count+=1
            if j!= len(board[0])-1 and board[i][j+1]==1:
                count+=1
            if count ==2 or count == 3:
                return False
            else:
                return True
        else:
            if board[i][j]==0:
                #diagonal top left to bottom right
                if i !=0 and j !=0 :
                    if board[i-1][j-1] == 1:
                        count+=1
                if i != len(board)-1 and j != len(board[0])-1:
                    if board[i+1][j+1] == 1:
                        count+=1
                #diagonal top right to bottom left
                if i!=0 and j != len(board[0])-1:
                    if board[i-1][j+1] ==1:
                        count+=1
                if i!= len(board)-1 and j!= 0:
                    if board[i+1][j-1] ==1:
                        count +=1
                #top and bottom vertically
                if i!=0 and board[i-1][j]==1:
                    count+=1
                if i!= len(board)-1 and board[i+1][j]==1:
                    count +=1
                #left and right horizontally
                if j!=0 and board[i][j-1] ==1:
                    count+=1
                if j!= len(board[0])-1 and board[i][j+1]==1:
                    count+=1
                if count == 3:
                    return True
                else:
                    return False