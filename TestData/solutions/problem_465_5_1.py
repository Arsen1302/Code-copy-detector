class Solution:
    # each state 6 len and 012345 permutation => (mn)! = 720 -> space = vis array of (mn)!
    def solution_465_5_1(self, board: List[List[int]]) -> int:
        
        def solution_465_5_2(board):
            return ''.join(str(x) for row in board  for x in row)
        
        # print(solution_465_5_2(board))
        
        def solution_465_5_3(state):
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
        
        parent = dict() 
        def solution_465_5_4(state):
            res = []
            while state in parent
                res.append(state)
                state = parent[state]
            return res
        
        # now template BFS...
        q = deque([solution_465_5_2(board)])
        dist = 0
        vis = set()
        while q: # level order traversal, expand one level at a time 
            # print(q)
            level_len = len(q)
            for _ in range(level_len):
                if q[0] == '123450':
                    return solution_465_5_4(q[0])
                
                parent_state = q[0]
                
                zx, zy = solution_465_5_3(q.popleft())
                # now check all four neighbours.. after swap what happens :)
                for x, y in [[zx,zy+1], [zx+1,zy],[zx,zy-1],[zx-1,zy]]:
                    if 0<=x<2 and 0<=y<3:
                        board[zx][zy], board[x][y] = board[x][y], board[zx][zy]
                        
                        kid_state = solution_465_5_2(board)
                        
                        parent[kid_state] = parent_state
                        
                        if state not in vis:
                            vis.add(state)
                            q.append(state)
                        board[zx][zy], board[x][y] = board[x][y], board[zx][zy]
            dist += 1
        
        return -1