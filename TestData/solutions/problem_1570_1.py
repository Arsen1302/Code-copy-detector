class Solution:
    def solution_1570_1(self, bottom: int, top: int, special: list[int]) -> int:
        special.sort()
        res = special[0] - bottom
        
        for i in range(1, len(special)):
            res = max(res, special[i] - special[i - 1] - 1)
            
        return max(res, top - special[-1])