class Solution:
    def solution_1037_2(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi)//2
            if arr[mid] - (mid + 1) < k: lo = mid + 1
            else: hi = mid
        return lo + k