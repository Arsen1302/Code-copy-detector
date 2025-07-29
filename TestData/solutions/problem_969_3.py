class Solution:
    def solution_969_3(self, n: int) -> List[str]:
        return [f"{x}/{d}" for d in range(1, n+1) for x in range(1, d) if gcd(x, d) == 1]