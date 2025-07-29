class Solution:
    def solution_104_3(self, nums: List[int]) -> bool:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 1
            else:
                return True
        return False