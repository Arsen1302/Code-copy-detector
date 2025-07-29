class Solution:
    def solution_1632_2(self, nums: List[int]) -> int:

        n = len(nums)
        res = []
        for i in range(n):
            res.append(nums[i] - i)

        a = Counter(res)
        ans = n * (n - 1) // 2
        for x in a:
            if a[x] > 1:
                ans -= a[x] * (a[x] - 1) // 2
        
        return ans