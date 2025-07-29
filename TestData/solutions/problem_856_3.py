class Solution:
    def solution_856_3(self, n: int) -> List[int]:
        res = [0] if n % 2 else []
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        return res