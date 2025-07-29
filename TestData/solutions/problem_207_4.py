class Solution:
    def solution_207_4(self, nums: List[int]) -> int:
        # 25 - 6 * (N - 1) + sum(nums) - 6 
        # cur - last_element * N + sum(nums)
        # eliminate overlapping sub-problem, no need re-calculation
        # only keep track last element

        N = len(nums)
        total = sum(nums)
        
        cur = 0
        for i in range(N):
            cur += i * nums[i]
        
        ret = cur
        for i in range(N - 1, -1, -1):
            cur = cur - nums[i] * N + total
            ret = max(ret, cur)
        
        return ret