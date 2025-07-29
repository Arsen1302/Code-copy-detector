class Solution:
    def solution_1138_2(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        N = len(nums)
        ans = []
        l_sum = 0
        l_covered = 0

        for i in range(N):
            r_size = N-i-1
            r_sum = total_sum - l_sum - nums[i]
            s = l_covered*nums[i] - l_sum + r_sum - r_size*nums[i]
            # print(i, l_covered*nums[i] - l_sum, r_sum - r_size*nums[i])
            ans.append(s)
            l_sum += nums[i]
            l_covered += 1

        return ans