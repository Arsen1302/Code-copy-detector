class Solution:
    def solution_936_5(self, nums: List[int]) -> List[int]:
        total, sub_sum = sum(nums), 0
        nums.sort(reverse=True)
        for i, n in enumerate(nums):
            sub_sum += n
            if 2 * sub_sum > total:
                return nums[:i + 1]
        return nums