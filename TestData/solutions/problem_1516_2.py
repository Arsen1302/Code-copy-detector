class Solution:
    def solution_1516_2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return nums[0]
        if k == 1:
            if n == 1:
                return -1
            else:
                return nums[1]
        if n == 1:
            if k % 2 != 0:
                return -1
            else:
                return nums[0]
        if k - n - 1 >= 0:
            return max(nums)
        if n == k:
            return max(nums[0:k - 1])
        if n > k:
            return max(max(nums[0:k - 1]), nums[k])