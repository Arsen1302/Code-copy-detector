class Solution:
    def solution_99_4_1(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = []
        res = set()

        trie = {}
        for word in words:
            current = trie
            for c in word:
                if c not in current:
                    current[c] = {}
                current = current[c]
            current['#'] = word      #to denote end of word

        def solution_99_4_2(r, c, seen, node):
            if '#' in node:
                res.add(node['#'])
                del node['#']

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and (nr, nc) not in seen and board[nr][nc] in node:
                    seen.append((nr, nc))
                    solution_99_4_2(nr, nc, seen, node[board[nr][nc]])
                    if len(node[board[nr][nc]]) == 0:
                        del node[board[nr][nc]]
                    seen.pop()


        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    seen.append((r, c))
                    solution_99_4_2(r, c, seen, trie[board[r][c]])
                    seen.pop()

        return list(res)