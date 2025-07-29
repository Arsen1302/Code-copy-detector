class Solution:
    def solution_1458_1(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)
        for i in asteroids:
            if i <= mass:
                mass += i
            else:
                return False
        return True