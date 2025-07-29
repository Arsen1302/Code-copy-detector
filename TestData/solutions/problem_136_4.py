class Solution:
    def solution_136_4(self, citations: List[int]) -> int:
        lo, hi = 0, len(citations)
        while lo < hi:
            mid = (lo + hi) // 2
            if citations[~mid] > mid:
                lo = mid + 1
            else:
                hi = mid
        return lo