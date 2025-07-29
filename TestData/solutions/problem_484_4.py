class Solution:
    def solution_484_4(self, board: List[str]) -> bool:
        Xs = Os = dia1 = dia2 = 0
        row = [0] * 3
        col = [0] * 3
        for r in range(3):
            for c in range(3):
                if board[r][c] == 'X':
                    Xs += 1
                    row[r] += 1
                    col[c] += 1
                    if c == r:
                        dia1 += 1
                    if c + r == 2:
                        dia2 += 1
                elif board[r][c] == 'O':
                    Os += 1
                    row[r] -= 1
                    col[c] -= 1
                    if c == r:
                        dia1 -= 1
                    if c + r == 2:
                        dia2 -= 1
           
        if max(max(row), dia1, dia2, max(col)) == 3: #X is winning, then O cannot win or cannot move after X wins
            if Xs == Os + 1 and min(min(row), dia1, dia2, min(col)) > -3:
                return True
        elif min(min(row), dia1, dia2, min(col)) == -3: #O is winning, then X cannot win or cannot move after X wins
            if Xs == Os and max(max(row), dia1, dia2, max(col)) < 3:
                return True
        else: #nobody is winning
            if ((Xs == Os) or (Xs == Os + 1)):
                return True
        return False