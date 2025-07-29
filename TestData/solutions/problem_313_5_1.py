class Solution:
    # Time: O(mn)
    # Space: O(mn)
    def solution_313_5_1(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click[0], click[1]
        if board[i][j] == "M":
            board[i][j] = "X"
            return board
        self.solution_313_5_2(board, i, j)
        return board
        
    def solution_313_5_2(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "E":
            return
        mines = self.solution_313_5_3(board, i, j)
        if mines > 0:
            board[i][j] = str(mines)
            return
        board[i][j] = "B"
        for x, y in self.directions:
            self.solution_313_5_2(board, i + x, j + y) 
    
    def solution_313_5_3(self, board, i, j):
        res = 0
        for x, y in self.directions:
            ni, nj = i + x, j + y
            if ni < 0 or ni >= len(board) or nj < 0 or nj >= len(board[0]):
                continue
            if board[ni][nj] == "M":
                res += 1
        return res
    
    def solution_313_5_4(self):
        self.directions = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]