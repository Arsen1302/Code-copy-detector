class Solution:
    def solution_1043_2(self, nums: List[int], target: int) -> int:
        d = {0:0}
        rangeListF = []
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            if sm - target in d:
                if len(rangeListF) == 0 or d[sm - target] > rangeListF[-1][1]:
                    rangeListF.append([d[sm - target], i])
                else:
                    pass
            d[sm] = i+1
        return len(rangeListF)