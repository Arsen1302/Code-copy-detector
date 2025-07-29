class Solution:
    def solution_1386_2(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n) - sum(rolls)
        if not n <= total <= 6*n: return []
        q, r = divmod(total, n)
        return [q]*(n-r) + [q+1]*r