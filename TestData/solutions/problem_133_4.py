class Solution:
    def solution_133_4(self, nums: List[int]) -> int:
        return list(set(range(0,len(nums)+1)).difference(set(nums)))[0]