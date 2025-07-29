class Solution:
    def solution_1469_5(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target != 1 and maxDoubles:
            if target % 2:
                target-=1
                moves+=1
            else:
                target//=2
                moves+=1
                maxDoubles-=1
        return moves + target-1