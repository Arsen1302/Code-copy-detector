class Solution:
    def solution_1352_1(self, nums: List[int]) -> int:
        gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
        return gcd(max(nums), min(nums))