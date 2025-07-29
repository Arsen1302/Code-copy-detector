class Solution:
    def solution_227_3(self, board: List[List[str]]) -> int:
        return sum(1 for i, row in enumerate(board) for j, cell in enumerate(row) if cell == "X" and (i == 0 or board[i - 1][j] == ".") and (j == 0 or board[i][j - 1] == "."))