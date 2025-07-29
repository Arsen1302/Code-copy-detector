class Solution:
    def solution_614_3_1(self, N: int) -> List[int]:
        nums = list(range(1, N+1))
        
        def solution_614_3_2(nums) -> List[int]:
            if len(nums) < 3:
                return nums
            even = nums[::2]
            odd = nums[1::2]
            return solution_614_3_2(even) + solution_614_3_2(old)
        return solution_614_3_2(nums)