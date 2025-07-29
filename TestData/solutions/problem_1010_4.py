class Solution:
    def solution_1010_4(self, n: int, left: List[int], right: List[int]) -> int:
        return max(n - min(right,default = n), max(left,default = 0))