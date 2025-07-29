class Solution:
    def solution_533_3(self, A: [int]) -> int:
        ret, cur, up = 0, 1, True
        for i in range(len(A) - 1):
            if A[i+1] == A[i]:
                ret, cur, up = max(cur, ret) if not up else ret, 1, True
                continue
            if up:
                cur += 1 if A[i+1] > A[i] else 0
                if cur <= 1:
                    continue
                if A[i+1] < A[i]:
                    cur, up = cur + 1, False
                    continue
            else:
                if A[i+1] > A[i]:
                    ret, cur, up = max(cur, ret), 1, True
                cur += 1
        return ret if (ret := max(ret, cur) if not up else ret) >= 3 else 0