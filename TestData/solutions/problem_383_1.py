class Solution:
    def solution_383_1(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')


- Python 3
- Junaid Mansuri