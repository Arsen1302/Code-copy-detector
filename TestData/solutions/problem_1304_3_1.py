class Solution:
    def solution_1304_3_1(self, nums: List[int]) -> int:
		n = len(nums)   
        @cache
        def solution_1304_3_2(i: int, p: bool) -> int:
            if i>=n:
                return 0 
			
			# if choose
            num = nums[i] if p else -nums[i]
            choose = num + solution_1304_3_2(i+1, not p)

            # if not choose
            not_choose = solution_1304_3_2(i+1, p)
            return max(choose, not_choose)

        return solution_1304_3_2(0, True)