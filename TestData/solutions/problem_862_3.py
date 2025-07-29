class Solution:
    def solution_862_3(self, W: List[List[str]], F: List[List[int]], ID: int, K: int) -> List[str]:
        A, V = set(F[ID]), set([ID])
        for _ in range(K-1):
            A = set(sum([F[a] for a in A],[])) - V - A
            V = V.union(A)
        C = collections.Counter(sorted(sum([W[a] for a in A], [])))
        return sorted(C.keys(), key = lambda x: C[x])
		
		
- Junaid Mansuri
- Chicago, IL