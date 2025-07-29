class Solution:
    def solution_465_1_1(self, board: List[List[int]]) -> int:
        def solution_465_1_2(board):
            if board[-1] != 0: return False
            for i in range(5):
                if board[i] != i + 1: return False
            return True
        
        swap = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }

        q = [board[0] + board[1]]
        steps = 0
        seen = set()
        while (len(q)):
            new_q = []
            for board in q:
                if tuple(board) in seen: continue
                seen.add(tuple(board))
                if solution_465_1_2(board): return steps

                zeroIdx = board.index(0)
                for swapIdx in swap[zeroIdx]:
                    copy = board.copy()
                    copy[zeroIdx], copy[swapIdx] = copy[swapIdx], copy[zeroIdx]
                    new_q.append(copy)
            steps += 1
            q = new_q

        return -1