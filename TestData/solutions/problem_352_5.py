class Solution:
    def solution_352_5(self, m: int, n: int, ops: List[List[int]]) -> int:
        for i in ops:
            m,n = min(m,i[0]), min(n,i[1])
        return m*n