class Solution:
    def solution_1706_1(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i%6==0:
                l.append(i)
        return sum(l)//len(l) if len(l)>0 else 0