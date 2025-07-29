class Solution:
    def solution_848_3(self, nums: List[int]) -> int:

        # output by generator expression
        return sum( (1 for number in nums if len(str(number))%2 == 0), 0 )