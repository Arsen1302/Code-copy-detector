class Solution:
    def solution_1467_1(self, plantTime: List[int], growTime: List[int]) -> int:
        res = 0
        for grow, plant in sorted(zip(growTime, plantTime)):
            res = max(res, grow) + plant
        return res