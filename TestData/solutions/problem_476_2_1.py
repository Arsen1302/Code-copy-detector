class Solution:
    def solution_476_2_1(self, arr: List[int], k: int) -> List[int]:
        N = len(arr)
        def solution_476_2_2(v):
            """1. the number of fractions < v
            2. the largest fraction l/r that is < v"""
            li = 0
            cnt, l, r = 0, arr[0], arr[-1]
            for ri in range(1, N):
                while li < ri and arr[li]/arr[ri] < v:
                    if arr[li]/arr[ri] > l/r:
                        l, r = arr[li], arr[ri]
                    li += 1
                cnt += li
            return cnt, l, r

        lo, hi = arr[0]/arr[-1], 1
        while lo <= hi:
            v = (lo+hi)/2
            cnt, l, r = solution_476_2_2(v)
            if cnt == k:
                return [l, r]
            if cnt < k:
                lo = v
            else:
                hi = v