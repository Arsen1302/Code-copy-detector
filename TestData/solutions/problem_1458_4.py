class Solution:
    def solution_1458_4(self, mass: int, asteroids: List[int]) -> bool:
        for x in sorted(asteroids): 
            if mass < x: return False 
            mass += x
        return True