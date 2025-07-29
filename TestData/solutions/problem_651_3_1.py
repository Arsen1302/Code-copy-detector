class Solution:
    def solution_651_3_1(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0:
            return []
        
        def solution_651_3_2(v):
            yield 1
            if v == 1:
                return
            vi = v
            while vi <= bound:
                yield vi
                vi *= v
        
        return list({xi + yi for xi in solution_651_3_2(x) for yi in solution_651_3_2(y) if xi + yi <= bound})