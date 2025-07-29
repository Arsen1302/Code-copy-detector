class Solution:
    def solution_1321_3(self, rungs: List[int], dist: int) -> int:
        newrungs = 0
        prev = 0
        
        for rung in rungs:
            diff = rung - prev - 1
            newrungs += diff // dist
            prev = rung
        
        return newrungs