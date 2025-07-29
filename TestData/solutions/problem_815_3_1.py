class Solution:
    def solution_815_3_1(self, n, s, res):
        if n == 0:
            res.append(s)
            return s
        s1 = self.solution_815_3_1(n-1, s^0, res)
        s2 = self.solution_815_3_1(n-1, s1^(1<<n-1), res)
        return s2
        
    def solution_815_3_2(self, n: int, start: int) -> List[int]:
        res = []
        self.solution_815_3_1(n, start, res)
        return res