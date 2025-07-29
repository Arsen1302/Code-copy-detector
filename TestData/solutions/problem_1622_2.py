class Solution:
    def solution_1622_2(self, nums: List[int]) -> int:
        return reduce(lambda acc,y: (acc[0],0) if y else (sum(acc)+1,acc[1]+1), nums, (0,0))[0]