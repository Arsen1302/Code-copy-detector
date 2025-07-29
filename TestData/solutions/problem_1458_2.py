class Solution:
    def solution_1458_2(self, mass: int, asteroids: List[int]) -> bool:
        # ///// TC O(nlogn) //////
        asteroids.sort()
        
        for asteroid in asteroids:
            if mass >= asteroid:
                mass += asteroid
            else:
                return False
        return True