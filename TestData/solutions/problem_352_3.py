class Solution:
    def solution_352_3(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min([x for x,y in ops])*min([y for x,y in ops]) if ops else m*n