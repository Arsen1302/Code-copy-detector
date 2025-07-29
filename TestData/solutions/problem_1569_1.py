class Solution:
    def solution_1569_1(self, w: List[str]) -> List[str]:
        return [next(g) for _, g in groupby(w, sorted)]