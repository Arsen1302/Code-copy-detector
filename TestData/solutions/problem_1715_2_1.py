class Solution:
    def solution_1715_2_1(self, low: int, high: int, zero: int, one: int) -> int:
        
        ans=[0]
        def solution_1715_2_2(s):
            if s>high:
                return 0
            p=solution_1715_2_2(s+zero)+solution_1715_2_2(s+one)
            if s>=low and s<=high:
                p+=1
            return p
        return solution_1715_2_2(0)%(10**9+7)