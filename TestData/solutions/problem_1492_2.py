class Solution:
    def solution_1492_2(self, beans: List[int]) -> int:
        beans.sort()
        n, s = len(beans), sum(beans) 
        return min(s - bag*(n - i) for i, bag in enumerate(beans))