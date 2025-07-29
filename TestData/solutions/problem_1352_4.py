class Solution:
    def solution_1352_4(self, nums: List[int]) -> int:
        import math
        return math.gcd(max(nums),min(nums))