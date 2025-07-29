class Solution:
    def solution_1367_3(self, rectangles: [[int]]) -> int:
        counter = Counter([i / j for i, j in rectangles])
        ans = 0
        for i, j in rectangles:
            ans += (counter.get(i / j) - 1)
            counter.update({i / j: - 1})
        return ans