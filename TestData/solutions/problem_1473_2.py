class Solution:
    def solution_1473_2(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = mn = mx = 0 
        for x in differences: 
            prefix += x
            mn = min(mn, prefix)
            mx = max(mx, prefix)
        return max(0, (upper-lower) - (mx-mn) + 1)