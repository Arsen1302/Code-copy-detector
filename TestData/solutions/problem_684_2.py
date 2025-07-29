class Solution:
    def solution_684_2(self, A: List[int], K: int) -> int:
        zero_index = [i for i, v in enumerate(A) if v == 0]
        if K >= len(zero_index):
            return len(A)
        res = 0
        for i in range(0, len(zero_index) - K + 1):
            one_start = zero_index[i-1] + 1 if i > 0 else 0
            one_end = zero_index[i+K] - 1 if i+K < len(zero_index) else len(A) - 1
            res = max(res, one_end - one_start + 1)
        return res