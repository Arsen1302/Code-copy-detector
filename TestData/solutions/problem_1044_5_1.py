class Solution:
    @cache
    def solution_1044_5_1(self, l, r):
        return 0 if l == r - 1 else min(self.solution_1044_5_1(l, i) + self.solution_1044_5_1(i, r) for i in range(l+1, r)) + self.cuts[r] - self.cuts[l]
    
    def solution_1044_5_2(self, n: int, cuts: List[int]) -> int:
        self.cuts = sorted(cuts + [0, n])
        return self.solution_1044_5_1(0, len(self.cuts) - 1)