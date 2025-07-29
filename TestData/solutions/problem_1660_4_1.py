class Solution:
    def solution_1660_4_1(self, s, e, k):
        if k <= 0:
            if k == 0 and s == e:
                return 1
            return 0
        if (s, k) in self.d:
            return self.d[(s, k)]
        self.d[(s, k)] = self.solution_1660_4_1(s+1, e, k-1) + self.solution_1660_4_1(s-1, e, k-1)
        return self.d[(s, k)]
    
    def solution_1660_4_2(self, startPos: int, endPos: int, k: int) -> int:
        self.d = {}
        return self.solution_1660_4_1(startPos, endPos, k) % (10**9 + 7)