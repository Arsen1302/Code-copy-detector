class Solution:
    def solution_614_2(self, n: int) -> List[int]:
        return sorted(range(1, n+1), key=lambda x: bin(x)[:1:-1])