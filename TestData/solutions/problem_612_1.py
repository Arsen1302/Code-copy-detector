class Solution:
    def solution_612_1(self, A: List[int], S: int) -> int:
        ans = prefix = 0
        seen = {0: 1}
        for x in A:
            prefix += x
            ans += seen.get(prefix - S, 0)
            seen[prefix] = 1 + seen.get(prefix, 0)
        return ans