class Solution(object):
    def solution_1138_4(self, nums):
        lSum, rSum, l, r = 0, sum(nums), 0, len(nums) - 1
        ans = []
        for n in nums:
            rSum -= n
            ans.append((n * l) - lSum + rSum - (n * r))
            lSum += n
            l += 1
            r -= 1
        return ans