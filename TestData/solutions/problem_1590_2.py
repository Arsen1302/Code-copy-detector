class Solution:
    def solution_1590_2(self, brackets: List[List[int]], income: int) -> float:
        brackets.sort(key=lambda x: x[0])
        res = 0 # Total Tax 
        prev = 0 # Prev Bracket Upperbound
        for u, p in brackets:
            if income >= u: # 
                res += ((u-prev) * p) / 100
                prev = u
            else:
                res += ((income-prev) * p) / 100
                break # As total income has been taxed at this point.
        return res