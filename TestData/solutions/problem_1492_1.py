class Solution:
    def solution_1492_1(self, beans: List[int]) -> int:
        beans.sort()
        return sum(beans) - max((len(beans)-i)*x for i, x in enumerate(beans))