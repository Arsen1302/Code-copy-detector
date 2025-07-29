class Solution:
    def solution_787_2(self, arr: List[int]) -> int:
        ans = d0 = d1 = -inf # delete 0 &amp; delete 1 element
        for x in arr:
            d0, d1 = max(x, x + d0), max(d0, x + d1)
            ans = max(ans, d0, d1)
        return ans