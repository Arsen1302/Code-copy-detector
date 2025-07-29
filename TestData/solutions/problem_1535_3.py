class Solution:
    def solution_1535_3(self, C: List[int], k: int) -> int:
        return bisect_left(range(1,sum(C)//k+1), True, key=lambda x:sum(c//x for c in C)<k)