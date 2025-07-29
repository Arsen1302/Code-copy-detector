class Solution:
    def solution_853_4(self, arr: List[int], target: int) -> int:
        start, end = 0, max(arr)
        res, mn, val = float("inf"), float("inf"), -1
        while start <= end:
            mid = (start + end)//2
            sums = 0
            for i in arr:
                sums += min(mid, i)
            val = abs(sums-target)
            if val == mn:
                res = min(res, mid)
            if val < mn:
                mn = val
                res = mid
            if sums >= target:
                end = mid-1
            else:
                start = mid+1
        return res