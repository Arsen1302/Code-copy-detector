class Solution:
    def solution_1615_5_1(self, start: str, target: str) -> bool:
        def solution_1615_5_2(s):
            for i, c in enumerate(s):
                if c != '_':
                    yield i, c
            yield -1, ' '
        
        for (si, sc), (ti, tc) in zip(solution_1615_5_2(start), solution_1615_5_2(target)):
            if sc != tc or (sc == 'L' and si < ti) or (sc == 'R' and si > ti):
                return False
        
        return True