class Solution:
    def solution_222_4(self, nums: List[int]) -> int:
        n, subs = len(nums), 0
        last_diff, count = None, 0
        for i in range(1, n):
            this_diff = nums[i] - nums[i - 1]
            if this_diff == last_diff:
                subs += count
                count += 1
            else:
                last_diff = this_diff
                count = 1
        return subs