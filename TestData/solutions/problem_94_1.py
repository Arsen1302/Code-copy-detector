class Solution:
    def solution_94_1(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]