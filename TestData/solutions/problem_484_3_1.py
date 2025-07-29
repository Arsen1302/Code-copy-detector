class Solution:
    def solution_484_3_1(self, board: List[str]) -> bool:
        row, col = len(board), len(board[0])
        xCount, oCount = 0, 0
        
        def solution_484_3_2(board):
            status = ''
            if board[0][2] == board[1][1] == board[2][0] !=' ':
                status = board[0][2]
            elif board[0][0] == board[1][1] == board[2][2] !=' ':
                status = board[0][0]
            elif board[0][0] == board[0][1] == board[0][2] !=' ':
                status = board[0][0]
            elif board[0][2] == board[1][2] == board[2][2] !=' ':
                status = board[0][2]
            elif board[2][2] == board[2][1] == board[2][0] !=' ':
                status = board[2][2]
            elif board[2][0] == board[1][0] == board[0][0] !=' ':
                status = board[2][0]
            elif board[0][1] == board[1][1] == board[2][1] !=' ':
                status = board[0][1]
            
            return status

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    xCount += 1
                elif board[i][j] == 'O':
                    oCount += 1

        if xCount < oCount or oCount+1 < xCount:
            return False
        
        status = solution_484_3_2(board)

        if status == 'X':
            return xCount == oCount+1
        if status == 'O':
            return xCount == oCount
        
        return True