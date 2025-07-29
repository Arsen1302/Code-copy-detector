class Solution:
    def solution_864_5(self, nums: List[int]) -> List[int]:
        res =[]
        for i in range(len(nums)//2):
            freq,val = nums[2*i] , nums[(2*i)+1]
            for j in range(freq+1):
                if j >=1 :
                    res.append(val)
        return res