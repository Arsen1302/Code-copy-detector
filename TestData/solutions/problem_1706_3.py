class Solution:
    def solution_1706_3(self, nums: List[int]) -> int:
        _ans =[]
        for i in nums:
            if (i%2==0) and (i%3==0):
                _ans.append(i)
        return sum(_ans)//len(_ans) if len(_ans) > 0 else 0