class Solution:
    def solution_313_4_1(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1),
                     (-1, -1), (1, -1), (1, 1), (-1, 1)] 
        
        def solution_313_4_2(mines, r, c):
            if r < 0 or r >= m  or c < 0 or c >= n or board[r][c] == 'M':
                return
            mines[r][c] += 1
        
        def solution_313_4_3(board, r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'E':
                return
            
            if mines[r][c] > 0:
                board[r][c] = str(mines[r][c])
                return 
            
            board[r][c] = 'B'
            for dr, dc in neighbors:
                solution_313_4_3(board, r + dr, c + dc)

        m = len(board)
        n = len(board[0]) 
        mines = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'M':
                    for dr, dc in neighbors:
                        solution_313_4_2(mines, r + dr, c + dc)        
       
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        elif board[r][c] == 'E':
            solution_313_4_3(board, r, c)
                
        return board