class Solution:
    def solution_43_4_1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        if rows <= 2:
            return board
        
        cols = len(board[0])
        if cols <= 2:
            return board
        
        def solution_43_4_2(i, j):
            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1:
                return
            
            if board[i][j] != 'O':
                return
            
            board[i][j] = '#'
            solution_43_4_2(i, j + 1)
            solution_43_4_2(i, j - 1)
            solution_43_4_2(i + 1, j)
            solution_43_4_2(i - 1, j)
        
        for i in range(rows):
            solution_43_4_2(i, 0)
            solution_43_4_2(i, cols - 1)
        
        for i in range(cols):
            solution_43_4_2(0, i)
            solution_43_4_2(rows - 1, i)
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'