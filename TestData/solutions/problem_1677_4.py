class Solution:
    def solution_1677_4(self, nums: List[int], k: int) -> List[int]:
        len_nums = len(nums)

        decreasing = [1] * len_nums
        left = nums[0]
        count = 0
        for i, n in enumerate(nums):
            if n <= left:
                count += 1
            else:
                count = 1
            left = n
            decreasing[i] = count

        increasing = [1] * len_nums
        right = nums[-1]
        count = 0
        for i in range(len_nums - 1, -1, -1):
            if nums[i] <= right:
                count += 1
            else:
                count = 1
            right = nums[i]
            increasing[i] = count

        return [i for i in range(k, len_nums - k)
                if decreasing[i - 1] >= k and increasing[i + 1] >= k]