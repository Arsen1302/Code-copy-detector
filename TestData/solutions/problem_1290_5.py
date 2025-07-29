class Solution:
    def solution_1290_5(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i, ck in enumerate(chalk):
            if k < ck:
                return i
            k -= ck
        return 0