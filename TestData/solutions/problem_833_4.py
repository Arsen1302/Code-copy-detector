class Solution:
    wins = [{(0, 0), (0, 1), (0, 2)}, {(1, 0), (1, 1), (1, 2)},
            {(2, 0), (2, 1), (2, 2)}, {(0, 0), (1, 0), (2, 0)},
            {(0, 1), (1, 1), (2, 1)}, {(0, 2), (1, 2), (2, 2)},
            {(0, 0), (1, 1), (2, 2)}, {(2, 0), (1, 1), (0, 2)}]

    def solution_833_4(self, moves: List[List[int]]) -> str:
        a, b = set(), set()
        for i, (r, c) in enumerate(moves):
            if i % 2:
                b.add((r, c))
                if any(win.issubset(b) for win in Solution.wins):
                    return "B"
            else:
                a.add((r, c))
                if any(win.issubset(a) for win in Solution.wins):
                    return "A"
        return "Pending" if len(moves) < 9 else "Draw"