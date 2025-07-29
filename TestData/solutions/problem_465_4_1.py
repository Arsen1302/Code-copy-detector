class Solution:
    def solution_465_4_1(self):
        self.memo = dict()
    def solution_465_4_2(self, board: List[List[int]]) -> int:
        def solution_465_4_3(board):
            return ''.join(str(x) for row in board  for x in row)
        
        # print(solution_465_4_3(board))
        
        def solution_465_4_4(state):
            si = 0
            zx, zy = 0, 0
            for row in range(2):
                for i in range(3):
                    board[row][i] = int(state[si])
                    if board[row][i] == 0:
                        zx,zy = row, i
                    si += 1
                    
            # returns the position of zero ;)
            return zx, zy
        
        # now BFS
        q = deque([solution_465_4_3(board)])
        dist = 0
        vis = set()
        
        while q:
            # print(q)
            level_len = len(q)
            for _ in range(level_len):
                if q[0] == '123450':
                    return dist
                zx, zy = solution_465_4_4(q.popleft())
                # now check all four neighbours.. after swap what happens :)
                for x, y in [[zx,zy+1], [zx+1,zy],[zx,zy-1],[zx-1,zy]]:
                    if 0<=x<2 and 0<=y<3:
                        board[zx][zy], board[x][y] = board[x][y], board[zx][zy]
                        state = solution_465_4_3(board)
                        if state not in vis:
                            vis.add(state)
                            q.append(state)
                        board[zx][zy], board[x][y] = board[x][y], board[zx][zy]
            dist += 1
        
        return -1