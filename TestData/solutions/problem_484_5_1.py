class Solution:
    def solution_484_5_1(self, board: List[str]) -> bool:
        X,O = self.solution_484_5_2(board)
        if O>X:
		    #Os can't  be greater than Xs
            return False
        elif abs(X-O)>1:
		    #Difference can only be 1 
            return False
        elif X>O:
		    #X can't have more moves than O if O is already won
            if self.solution_484_5_3(board,'O'): return False
        else:
		    #X and O can't have equal moves if X is winning
            if self.solution_484_5_3(board,'X'): return False
        return True
            
    
    def solution_484_5_2(self, board):
        X = 0
        O = 0
        for row in board:
            for i in row:
                if i == 'X':
                    X+=1
                elif i == 'O':
                    O+=1
        return X,O
                    
    def solution_484_5_3(self, board, sym='X'):
        #Checking for Hight triads
        i = 0
        while i<3:
            if (board[0][i] == board[1][i] == board[2][i] == sym):
                return True
            i+=1
            
        #Checking for width
        i=0
        while i<3:
            if (board[i][0] == board[i][1] == board[i][2] == sym):
                return True
            i+=1
            
        #Checking for diag.
        if (board[0][0] == board[1][1] == board[2][2] == sym):
                return True
        if (board[0][2] == board[1][1] == board[2][0] == sym):
                return True
        return False