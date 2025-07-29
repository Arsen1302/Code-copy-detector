class Solution:
    def solution_1467_4(self, plantTime: List[int], growTime: List[int]) -> int:
        plant_finish = grow_finish = 0
        for grow, plant in sorted(zip(growTime, plantTime), reverse=True):
            plant_finish += plant
            grow_finish = max(grow_finish, plant_finish + grow)

        return grow_finish