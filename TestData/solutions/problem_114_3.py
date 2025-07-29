class Solution:
    def solution_114_3(self, nums: List[int]) -> List[str]:
        begin, res = 0, []
        for i in range(len(nums)):
            if i + 1 >=len(nums) or nums[i+1]-nums[i] != 1:
                b = str(nums[begin])
                e =  str(nums[i])
                res.append(b + "->" + e if b != e else b)
                begin = i + 1
        return res