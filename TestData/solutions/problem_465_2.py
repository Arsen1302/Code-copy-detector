class Solution:
    def solution_465_2(self, board: List[List[int]]) -> int:
        neighbours = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        board = tuple(tile for row in board for tile in row)
        solved = (1, 2, 3, 4, 5, 0)
        
        if board == solved:
            return 0
        
        q = collections.deque([(board, 0)])
        visited = {board}
        
        while q:
            board, moves = q.popleft()
            zero = board.index(0)
            
            for neighbour in neighbours[zero]:
                newBoard = list(board)
                newBoard[zero], newBoard[neighbour] = newBoard[neighbour], newBoard[zero]
                newBoard = tuple(newBoard)
                
                if newBoard == solved:
                    return moves + 1
                if newBoard not in visited:
                    visited.add(newBoard)
                    q.append((newBoard, moves + 1))
        
        return -1