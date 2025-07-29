class Solution:
    def solution_1660_3_1(self, s, e, k):
        if k == 0:
            if s == e:
                return 1
            return 0
        return self.solution_1660_3_1(s+1, e, k-1) + self.solution_1660_3_1(s-1, e, k-1)
    
    def solution_1660_3_2(self, startPos: int, endPos: int, k: int) -> int:
        return self.solution_1660_3_1(startPos, endPos, k) % (10**9 + 7)