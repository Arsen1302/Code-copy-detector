class Solution:
    def solution_1585_4(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        pos = {}
        for i in range(len(nums)):
            pos[nums[i]] = i
            
        for i,j in operations:
            index = pos[i]
            nums[index] = j
            pos[j] = index
            pos.pop(i)
        return nums