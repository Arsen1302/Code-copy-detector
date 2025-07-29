class Solution:
    def solution_1692_2(self, nums: List[int]) -> int:
        max_ = sum_ = 0
		
        for i, num in enumerate(nums, start = 1):
            sum_ += num
            ave, modulo = divmod(sum_, i)
            if modulo: ave += 1
            max_ = max(ave, max_)

        return max_
    # end solution_1692_2()