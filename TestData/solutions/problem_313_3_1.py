class Solution:    
    def solution_313_3_1(self, board, row, col):
        n, m = len(board), len(board[0])
        
        for dr, dc in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
            newRow = row + dr
            newCol = col + dc
            
            if newRow >= 0 and newRow < n and newCol >= 0 and newCol < m:
                yield (newRow, newCol)
    
    def solution_313_3_2(self, board, row, col):
        mines = 0
        
        for newRow, newCol in self.solution_313_3_1(board, row, col):
            mines += 1 if board[newRow][newCol] == 'M' else 0
        
        return mines
    
    def solution_313_3_3(self, board, row, col):
        queue = collections.deque([(row, col)])
        
        while queue:
            row, col = queue.popleft()
            
            if board[row][col] == 'E':
                minesAround = self.solution_313_3_2(board, row, col)
                
                if minesAround > 0:
                    board[row][col] = str(minesAround)
                else:
                    board[row][col] = 'B'
                    
                    for newRow, newCol in self.solution_313_3_1(board, row, col):
                        if board[newRow][newCol] == 'E':
                            queue.append((newRow, newCol))
        
    def solution_313_3_4(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click
        
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            self.solution_313_3_3(board, row, col)
            
        return board