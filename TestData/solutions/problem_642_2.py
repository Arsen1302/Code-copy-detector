class Solution:
    def solution_642_2(self, nums: List[int]) -> int:
        
        set1 = set()
        for i in nums :
            if i in set1 :
                return i
            else :
                set1.add(i)