class Solution:
    def solution_467_3_1(self, start: str, end: str) -> bool:
        def solution_467_3_2(s):
            for i, c in enumerate(s):
                if c != 'X':
                    yield i, c
            
            yield -1, ' '
        
        for (startI, startC), (endI, endC) in zip(solution_467_3_2(start), solution_467_3_2(end)):
            if (startC != endC or
                (startC == 'L' and startI < endI) or
                (startC == 'R' and startI > endI)):
                return False
        
        return True