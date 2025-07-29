class Solution:
    def solution_933_4(self, s: str, k: int) -> bool:

        D = defaultdict(int)
        for x in s:
            D[x] = (D[x] + 1)%2

        if sum(list(D.values())) <= k and len(s) >= k:
            return True

        return False