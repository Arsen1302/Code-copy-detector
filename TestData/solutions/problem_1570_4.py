class Solution:
    def solution_1570_4(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        
        special_floors=[bottom-1] + special + [top+1]
        
        res = 0
        for i in range(1, len(special_floors)):
            res = max(res, special_floors[i] - special_floors[i-1] - 1)            
        
        return res