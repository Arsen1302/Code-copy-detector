class Solution:
    def solution_925_3(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            arr.insert(index[i] , nums[i])
        return arr