class Solution:
    def solution_628_3_1(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rank = [1] * n
        parent = [i for i in range(n)]
        
        def solution_628_3_2(i, j):
            i, j = solution_628_3_3(i), solution_628_3_3(j)
            if i == j:
                return 0
            if rank[i] < rank[j]:
                i, j = j, i
            rank[i] += rank[j]
            parent[j] = parent[i]
            return 1
        
        def solution_628_3_3(i):
            while i != parent[i]:
                parent[i] = i = parent[parent[i]]
            return i
        
        rows, cols = {}, {}
        removed = 0
        for i, (row, col) in enumerate(stones):
            if row in rows:
                removed += solution_628_3_2(i, rows[row])
            else:
                rows[row] = i
            if col in cols:
                removed += solution_628_3_2(i, cols[col])
            else:
                cols[col] = i
        
        return removed