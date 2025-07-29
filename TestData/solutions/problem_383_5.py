class Solution:
    def solution_383_5(self, moves: str) -> bool:
        direction = {
            'U': 1j,
            'D': -1j,
            'L': -1,
            'R': 1,
        }
        return sum(direction[m] for m in moves) == 0