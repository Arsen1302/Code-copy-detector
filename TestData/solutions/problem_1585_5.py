class Solution:
    def solution_1585_5(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        idxDict = {}

        for i in range(len(nums)):
            idxDict[nums[i]] = i

        for a,b in operations:
            idx = idxDict[a]
            idxDict.pop(a)
            idxDict[b] = idx

        for k in idxDict:
            nums[idxDict[k]] = k

        return nums