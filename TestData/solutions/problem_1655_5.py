class Solution:
    def solution_1655_5(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(0,len(nums)-1):
            s = nums[i] + nums[i+1]
            if s in dic:
                return True
            dic[s] = i
        return False