class Solution:
    def solution_409_5(self, W: List[str], k: int) -> List[str]:
        C = collections.Counter(W)
        S = sorted(C.keys(), key = lambda x: [-C[x],x])
        return S[:k]