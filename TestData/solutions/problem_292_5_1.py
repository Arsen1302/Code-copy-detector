class Solution:
    def solution_292_5_1(self, nums: List[int]) -> List[int]:
        def solution_292_5_2(num,arr):
            for i in arr:
                if i>num:
                    return i
            else:
                return -1     
        ans = []
        for i in range(len(nums)):
            ans.append(solution_292_5_2(nums[i],nums[i:]+nums[:i]))
        return ans