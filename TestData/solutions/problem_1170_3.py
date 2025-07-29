class Solution:
    def solution_1170_3(self, nums: List[int]) -> int:
        product_count = collections.defaultdict(int)
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1
        res = 0
        for k, v in product_count.items():
            if v > 1:
                res += (v*(v-1)//2) * (2**3)
        return res