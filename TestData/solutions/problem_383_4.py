class Solution:
    def solution_383_4(self, moves: str) -> bool:
        x, y = 0, 0
        
        for i in moves.lower():
            if i == 'u':
                y += 1
            elif i == 'r':
                x += 1
            elif i == 'd':
                y -= 1
            elif i == 'l':
                x -= 1
        return x == 0 and y == 0