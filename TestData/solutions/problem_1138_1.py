class Solution:
    def solution_1138_1(self, nums: List[int]) -> List[int]:
        pre_sum = [0]
        for num in nums:                                     # calculate prefix sum
            pre_sum.append(pre_sum[-1] + num)
        n = len(nums)                                        # render the output
        return [(num*(i+1) - pre_sum[i+1]) + (pre_sum[-1]-pre_sum[i] - (n-i)*num) for i, num in enumerate(nums)]