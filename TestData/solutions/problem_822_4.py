class Solution:
    def solution_822_4(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = collections.defaultdict(lambda: False)
        cols = collections.defaultdict(lambda: False)
        for i, j in indices:
            rows[i] = not rows[i]
            cols[j] = not cols[j]
        
        return sum(rows[i] != cols[j] for i in range(m) for j in range(n))