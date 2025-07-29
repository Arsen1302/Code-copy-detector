class Solution:
    def solution_679_4(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    count = 0;
                    l, r = j - 1, j + 1
                    while l >= 0:
                        if board[i][l] in 'pB':
                            count += board[i][l] == 'p'
                            break
                        l -= 1
                    while r < len(board[0]):
                        if board[i][r] in 'pB':
                            count += board[i][r] == 'p'
                            break
                        r += 1
                    u, d = i - 1, i + 1
                    while u >= 0:
                        if board[u][j] in 'pB':
                            count += board[u][j] == 'p'
                            break
                        u -= 1
                    while d < len(board):
                        if board[d][j] in 'pB':
                            count += board[d][j] == 'p'
                            break
                        d += 1
                    return count