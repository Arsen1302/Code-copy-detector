class Solution:
    def solution_1321_2(self, rungs: List[int], dist: int) -> int:
        newrungs = 0
        prev = 0
        
        for rung in rungs:
            diff = rung - prev
            
            if diff > dist:
                add = diff / dist # Number of rungs we need to add
                
                if add % 1 == 0:
                    add = int(add) - 1
                else:
                    add = int(add)
                newrungs += add
            prev = rung
        
		return newrungs