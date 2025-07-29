class Solution:
    def solution_383_3(self, moves: str) -> bool:
        moveMap = {
            'R' : [0, 1],
            'L' : [0, -1],
            'U' : [1, 0],
            'D' : [-1, 0]
        }
        startX = 0
        startY = 0
        
        for move in moves:
            direction = moveMap[move]
            startX += direction[0]
            startY += direction[1]
        
        if [startX, startY] == [0, 0]:
            return True
        else:
            return False