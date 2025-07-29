class Solution:
    def solution_1458_5(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for i in asteroids:
            if mass >= i:
                mass += i
            else:
                return False
        return True