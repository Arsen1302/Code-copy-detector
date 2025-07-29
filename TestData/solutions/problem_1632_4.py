class Solution:
    def solution_1632_4(self, nums: List[int]) -> int:
        res = 0
        d = defaultdict(int)
        l = len(nums)
        total = l*(l-1)//2
        for i,n in enumerate(nums):
            res += d[n-i]
            d[n-i] += 1
        return total - res