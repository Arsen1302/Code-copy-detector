class Solution:
    def solution_1382_5(self, nums: List[str], target: str) -> int:
        count, len_nums = 0, len(nums)
        for i in range(len_nums - 1):
            for j in range(i + 1, len_nums):
                if nums[i] + nums[j] == target:
                    count += 1
                if nums[j] + nums[i] == target:
                    count += 1
        return count