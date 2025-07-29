class Solution:
    def solution_1186_4_1(self, nums: List[int]) -> int:
        def solution_1186_4_2(nums: List[int]) -> int:
            result, total = nums[0], 0
            for num in nums:
                total += num
                if total < 0: total = 0
                result = max(result, total)
            return result
        invNums = [-num for num in nums]
        return max(solution_1186_4_2(nums), solution_1186_4_2(invNums))