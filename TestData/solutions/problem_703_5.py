class Solution:
    def solution_703_5(self, queries: List[str], pattern: str) -> List[bool]:
        P = len(pattern)
        res = [False]*len(queries)
        for i, query in enumerate(queries):
            p = q = 0
            Q = len(query)
            while q < Q and p < P:
                if query[q] == pattern[p]:
                    q, p = q + 1, p + 1
                elif query[q].islower():
                    q = q + 1
                else:
                    break
            if (q == Q and p == P) or (query[q:].islower() and p == P):
                res[i] = True
        return res