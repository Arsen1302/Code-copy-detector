class Solution:
    def solution_1010_2(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left,default=0), n - min(right, default=n))