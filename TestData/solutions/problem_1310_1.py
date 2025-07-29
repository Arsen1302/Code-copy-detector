class Solution:
    def solution_1310_1(self, dist: List[int], speed: List[int]) -> int:
        for i, t in enumerate(sorted((d+s-1)//s for d, s in zip(dist, speed))): 
            if i == t: return i
        return len(dist)