class Solution:
    def solution_1566_2(self, nums: List[int]) -> int:
        lsum, rsum, ans = 0, sum(nums), 0
        for i in range(len(nums) - 1):
            lsum += nums[i]
            rsum -= nums[i]
            ans += (lsum >= rsum)
        return ans