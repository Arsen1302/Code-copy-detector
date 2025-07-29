class Solution:
    def solution_1185_2(self, nums: List[int]) -> int:
        uniq = []
        [uniq.append(num) for num in nums if nums.count(num) == 1]
        return sum(uniq)