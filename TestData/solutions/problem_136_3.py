class Solution:
    def solution_136_3(self, citations: List[int]) -> int:
        n = len(citations)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi)//2
            if citations[mid] < n - mid:
                lo = mid + 1
            else:
                hi = mid
        return n - lo