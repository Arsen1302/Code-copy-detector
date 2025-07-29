class Solution:
    def solution_189_3_1(self, start, end):
        if start >= end:
            return 0
        if (start, end) in self.d:
            return self.d[(start, end)]
        self.d[(start, end)] = float("inf")
        for i in range(start, end+1):
            cost1 = self.solution_189_3_1(start, i-1) + i
            cost2 = self.solution_189_3_1(i+1, end) + i
            cost = max(cost1, cost2)
            self.d[(start, end)] = min(self.d[(start, end)], cost)
        return self.d[(start, end)]
    
    def solution_189_3_2(self, n: int) -> int:
        self.d = {}
        return self.solution_189_3_1(1, n)