class Solution:
    def solution_1430_5(self, nums: List[int], k: int) -> List[int]:
        x = 2*k + 1
        n = len(nums)
        if x > n:
            return [-1] * n
        
        s = sum(nums[i] for i in range(x))
        res = [-1] * k + [s // x]

        for i in range(k + 1, n - k):
            s += nums[i + k] - nums[i - k - 1]
            res.append(s // x)
        
        res.extend([-1] * k)
        return res